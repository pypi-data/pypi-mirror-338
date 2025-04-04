import argparse
import copy
import dataclasses
import functools
import itertools
import pathlib
from typing import Type

import tomli
import yaml

import vorbote.schema


@dataclasses.dataclass
class Tag:
    name: str
    type: type = list[str]
    sorted: bool = False

    def to_field(self) -> tuple[str, Type, dataclasses.Field]:
        """Transform Tag instance into a dataclass field definition"""
        values = (
            self.name,
            self.type,
            dataclasses.field(
                default_factory=self.type, metadata={"sorted": self.sorted}
            ),
        )

        return values


@dataclasses.dataclass(init=False, repr=False)
class Config:
    def __init__(self, parent: str = "", **kwargs):
        for k, v in kwargs.items():
            if parent == "tags" and k == "sorted":
                setattr(self, k, [Tag(name=t, sorted=True) for t in v] if v else [])
            elif parent == "tags" and k == "unsorted":
                setattr(self, k, [Tag(name=t, sorted=False) for t in v] if v else [])
            elif isinstance(v, dict):
                setattr(self, k, Config(parent=k, **v))
            else:
                setattr(self, k, v)

    @classmethod
    def from_file(cls, path: pathlib.Path | str, validate: bool = True) -> "Config":
        """Load config from YAML config file"""
        path = pathlib.Path(path)

        schema_path = (
            pathlib.Path(__file__).parent.joinpath("schemas").joinpath("config.schema")
        )

        loaders = {
            ".yaml": functools.partial(yaml.load, Loader=yaml.Loader),
            ".toml": tomli.load,
        }

        if path.suffix in loaders:
            with open(path, mode="rb") as infile:
                data = loaders[path.suffix](infile)
        else:
            raise TypeError(f"Invalid config format, suffix='{path.suffix}'")

        if validate:
            vorbote.schema.validate(path=schema_path, data=data)

        return cls(**data)

    @classmethod
    def from_args(cls, args: argparse.Namespace) -> "Config":
        top_level = ["annotations", "config"]

        options = [
            (k.split("_", maxsplit=1), v)
            for k, v in sorted(vars(args).items())
            if k != "help"
        ]

        grouped = [
            (k, {x[0][-1]: x[1] for x in g})
            for k, g in itertools.groupby(
                sorted(options, key=lambda x: x[0]), key=lambda x: x[0][0]
            )
        ]

        kwargs = {k: v[k] if k in top_level else v for k, v in grouped}

        return cls(**kwargs)

    def get(self, *args: str):
        """Get value at path as defined by args (left to right descending)"""
        result = functools.reduce(lambda a, b: getattr(a, b, self), args, self)

        return result if result != self else None

    def merge(self, config: "Config", parent: str = "") -> "Config":
        """Merge Config values from another instance into this Config"""
        left = copy.deepcopy(self)

        for k, v in vars(left).items():
            if type(v) == type(left):
                setattr(left, k, v.merge(config=config, parent=k))
            elif parent:
                setattr(left, k, config.get(parent, k) or v)
            else:
                setattr(left, k, config.get(k) or v)

        return left

    def __repr__(self) -> str:
        _values = ", ".join([f"{k}={str(v)}" for k, v in vars(self).items()])

        return f"{type(self).__name__}({_values})"
