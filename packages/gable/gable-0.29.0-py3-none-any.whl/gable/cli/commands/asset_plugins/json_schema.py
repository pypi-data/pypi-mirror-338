import functools
import json
import re
from pathlib import Path
from typing import Any, Callable, List, Mapping, TypedDict

import click
import jsonref
from gable.api.client import GableAPIClient
from gable.cli.commands.asset_plugins.baseclass import (
    AssetPluginAbstract,
    ExtractedAsset,
)
from gable.cli.helpers.emoji import EMOJI
from gable.cli.helpers.repo_interactions import get_git_repo_info, get_git_ssh_file_path
from gable.openapi import SourceType, StructuredDataAssetResourceName

JsonSchemaConfig = TypedDict(
    "JsonSchemaConfig",
    {
        "files": list[click.Path],
    },
)


class JsonSchemaAssetPlugin(AssetPluginAbstract):
    def source_type(self) -> SourceType:
        return SourceType.json_schema

    def click_options_decorator(self) -> Callable:
        def decorator(func):
            @click.argument(
                "files",
                nargs=-1,
                type=click.Path(exists=True, file_okay=True, dir_okay=False),
                required=True,
            )
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def click_options_keys(self) -> set[str]:
        return set(JsonSchemaConfig.__annotations__.keys())

    def pre_validation(self, config: Mapping) -> None:
        # todo: unnecssary? test
        typed_config = JsonSchemaConfig(**config)
        if not typed_config["files"]:
            raise click.MissingParameter(
                f"{EMOJI.RED_X.value} At least one JSON schema file is required.",
                param_type="option",
            )

    def extract_assets(
        self, client: GableAPIClient, config: Mapping
    ) -> List[ExtractedAsset]:
        typed_config = JsonSchemaConfig(**config)
        """Extract assets from the source."""
        from recap.converters.json_schema import JSONSchemaConverter
        from recap.types import UnionType

        files_list: list[click.Path] = list(typed_config["files"])
        source_names: list[str] = []
        schema_contents_raw: list[str] = []
        for file_path in files_list:
            file_path_abs = Path(str(file_path)).absolute()
            try:
                # Resolve any local JSON references before sending the schema
                with file_path_abs.open() as file_contents:
                    result = jsonref.load(
                        file_contents,
                        base_uri=file_path_abs.as_uri(),
                        jsonschema=True,
                        proxies=False,
                    )
                    schema_contents_raw.append(jsonref.dumps(result))
            except Exception as exc:
                raise click.ClickException(
                    f"{file_path}: Error parsing JSON Schema file, or resolving local references: {exc}"
                ) from exc
            source_names.append(
                get_git_ssh_file_path(get_git_repo_info(str(file_path)), str(file_path))
            )

        if len(schema_contents_raw) == 0:
            raise click.ClickException(
                f"{EMOJI.RED_X.value} No data assets found to register! You can use the --debug or --trace flags for more details.",
            )

        extracted_assets: list[ExtractedAsset] = []
        for source_name, schema_content_raw in zip(source_names, schema_contents_raw):
            schema_recap_types = JSONSchemaConverter().to_recap(schema_content_raw)
            data_asset_name = get_json_schema_title(schema_content_raw) or "object"
            extracted_fields = []
            for field in schema_recap_types.fields:
                if "name" not in field.extra_attrs and isinstance(field, UnionType):
                    field.extra_attrs["name"] = "union"
                extracted_fields.append(
                    ExtractedAsset.safe_parse_field(recap_type_to_dict(field))
                )
            extracted_assets.append(
                ExtractedAsset(
                    darn=StructuredDataAssetResourceName(
                        source_type=self.source_type(),
                        data_source=source_name,
                        path=data_asset_name,
                    ),
                    dataProfileMapping=None,
                    fields=extracted_fields,
                )
            )
        return extracted_assets

    def checked_when_registered(self) -> bool:
        return False


def get_json_schema_title(schema: str) -> str | None:
    json_schema = json.loads(schema)

    if "title" in json_schema:
        # Remove whitespace from the title if it exists using regex
        title = re.sub(r"\s+", "", json_schema["title"])
        return title
    else:
        return None


RECAP_TYPE_REGISTRY = None


def recap_type_to_dict(recap_type) -> dict[str, Any]:
    """
    Converts a RecapType to a dictionary

    Despite being called 'to_dict', this function can return a dictionary, a list or a
    string. This is a wrapper function to convert the output of to_dict() to a
    dictionary.

    This should take a RecapType, but we can't annotate the function because we want to only import that inside the function
    """
    from recap.types import RecapType, RecapTypeRegistry, alias_dict, to_dict

    recap_type_asserted: RecapType = recap_type

    global RECAP_TYPE_REGISTRY
    # Initialize this inside the function so we don't have to import the constructor at the top of the file
    RECAP_TYPE_REGISTRY = RECAP_TYPE_REGISTRY or RecapTypeRegistry()

    # Run alias_dict() separately so we can use a shared RecapTypeRegistry, otherwise
    # a new instance of the class is created for each call which kills performance
    recap_type_to_dict_output = to_dict(recap_type_asserted, True, False)
    if isinstance(recap_type_to_dict_output, list):
        type_dict = {"type": "union", "types": recap_type_to_dict_output}
    elif isinstance(recap_type_to_dict_output, str):
        type_dict = {"type": recap_type_to_dict_output}
    else:
        if recap_type_to_dict_output.get("type", None) is None:
            recap_type_to_dict_output["type"] = "unknown"
        type_dict = recap_type_to_dict_output
    type_dict = alias_dict(type_dict, RECAP_TYPE_REGISTRY)
    return type_dict
