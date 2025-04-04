import json
import pathlib

import jsonschema


def validate(path: pathlib.Path | str, data: dict) -> None:
    """Validate data against a predefined JSON schema"""
    with open(pathlib.Path(path), mode="r", encoding="utf-8") as infile:
        schema = json.load(infile)

    validator = jsonschema.Draft7Validator(
        schema=schema, format_checker=jsonschema.FormatChecker()
    )

    validator.validate(data)
