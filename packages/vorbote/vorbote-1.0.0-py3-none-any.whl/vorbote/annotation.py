import abc
import dataclasses
import datetime
import functools
import hashlib
import inspect
import itertools
import pathlib
from typing import Any, Type

import yaml

import vorbote.parse
import vorbote.schema
from vorbote.config import Config


class AnnotationMeta:
    @classmethod
    @abc.abstractmethod
    def from_yaml(cls, **kwargs) -> Type["AnnotationMeta"]:  # pragma: no cover
        """Parse YAML key/value pairs into class instance"""
        pass


class Author(vorbote.parse.Author, AnnotationMeta):
    @classmethod
    def from_yaml(cls, name: str, email: str) -> "Author":
        """Parse YAML key/value pairs into class instance"""
        return cls(name=name, email=email)


class Tag(vorbote.parse.Impact, AnnotationMeta):
    @classmethod
    def from_yaml(cls, **kwargs) -> "Tag":
        """Parse YAML key/value pairs into class instance"""
        return cls(**kwargs)


@dataclasses.dataclass
class Ticket(AnnotationMeta):
    tagline: str
    description: str = ""

    @classmethod
    def from_yaml(cls, tagline: str, **kwargs) -> "Ticket":
        """Parse YAML key/value pairs into class instance"""
        return cls(tagline=tagline, **kwargs)


@dataclasses.dataclass
class Story(AnnotationMeta):
    reference: str
    tickets: list[Ticket]
    authors: list[Author] = dataclasses.dataclass(init=False)
    impact: Tag = dataclasses.dataclass(init=False)

    @classmethod
    def from_yaml(cls, reference: str, tickets: list[dict]) -> "Story":
        """Parse YAML key/value pairs into class instance"""
        _tickets = [Ticket.from_yaml(**kw) for kw in tickets]

        return cls(reference=reference, tickets=_tickets)

    @functools.cached_property
    def ticket(self) -> vorbote.parse.Ticket:
        """Return a ticket reference for a story"""
        return vorbote.parse.Ticket.from_reference(self.reference)

    @functools.cached_property
    def key(self) -> str:
        """Return a unique identifier for a story"""
        return self.ticket.reference

    @functools.cached_property
    def messages(self) -> list[vorbote.parse.Message]:
        """Return all commits that belong to a story"""
        _messages = []

        for t in self.tickets:
            _hash = hashlib.sha1()
            _hash.update(f"{t.tagline}\n{t.description}".encode("utf-8"))

            _message = vorbote.parse.Message(
                tagline=t.tagline,
                descriptions=t.description.split("\n"),
                impact=self.impact,
                epic=None,
                ticket=self.ticket,
                sha=_hash.hexdigest(),
                author=None,
                timestamp=datetime.datetime.now(),
            )
            _message.qualified = True

            _messages.append(_message)

        return _messages

    @functools.cached_property
    def hashes(self) -> list[str]:
        """Gather all subordinate commit hashes"""
        return [x.sha for x in self.messages]

    def __hash__(self) -> int:  # pragma: no cover
        return hash(self.key)

    def __eq__(self, other: Any) -> bool:  # pragma: no cover
        return self.key == other

    def __lt__(self, other: Any) -> bool:  # pragma: no cover
        return self.key < other

    def __gt__(self, other: Any) -> bool:  # pragma: no cover
        return self.key > other

    def __str__(self) -> str:
        return self.key


@dataclasses.dataclass
class Epic(AnnotationMeta):
    name: str
    authors: list[Author] = dataclasses.field(default_factory=list)
    description: str | None = None
    stories: list[Story] = dataclasses.field(default_factory=list)
    tags: list[Tag] = dataclasses.field(default_factory=Tag)

    @classmethod
    def from_yaml(cls, config: Config, **kwargs) -> "Epic":
        """Parse YAML key/value pairs into class instance"""
        _parsers = {
            "authors": Author,
            "stories": Story,
            "tags": Tag.from_config(config=config),
        }

        _kwargs = {}

        for k, v in kwargs.items():
            if k in _parsers and isinstance(v, list):
                _kwargs[k] = [_parsers[k].from_yaml(**kw) for kw in v]
            elif k in _parsers and isinstance(v, dict):
                _kwargs[k] = _parsers[k].from_yaml(**v)
            else:
                _kwargs[k] = v

        return cls(**_kwargs)

    def merge_stories(self) -> "Epic":
        """Merge author/impact information into child stories"""
        for idx, s in enumerate(self.stories):
            s.authors = self.authors
            s.impact = self.tags if idx == 0 else type(self.tags)()

        return self

    @property
    def impact(self) -> list[Tag]:
        return self.tags


@dataclasses.dataclass(init=False, kw_only=True)
class AnnotationsMeta:
    _impact_class: Type[vorbote.parse.Impact] = dataclasses.field(init=False)
    _parsers: dict[str, Type[AnnotationMeta]] = dataclasses.field(
        default_factory=dict, init=False
    )

    def __init_subclass__(
        cls, parsers: dict[str, Type[AnnotationMeta]] | None = None, **kwargs
    ):  # pragma: no cover
        cls._parsers = parsers or {"epics": Epic}

    def __init__(self, config: Config, **kwargs: list[dict]):
        for k, v in kwargs.items():
            if k in self._parsers:
                _init: AnnotationMeta = self._parsers[k]
            else:
                _init: Type = dataclasses.make_dataclass(
                    k.capitalize(),
                    sorted(
                        set.union(
                            *[{(_k, type(_v)) for _k, _v in x.items()} for x in v]
                        )
                    ),
                    bases=(AnnotationMeta,),
                )
                _init.from_yaml = classmethod(lambda _cls, **kw: _cls(**kw))

            if "config" in inspect.signature(_init.from_yaml).parameters:
                setattr(self, k, [_init.from_yaml(config=config, **kw) for kw in v])
            else:
                setattr(self, k, [_init.from_yaml(**kw) for kw in v])

        for f in dataclasses.fields(self):
            if f.name not in kwargs and f.init:
                setattr(self, f.name, [])

        self._impact_class = vorbote.parse.Impact.from_config(config=config)

    def merge(
        self, *args: vorbote.parse.Changes | Type["AnnotationMeta"]
    ) -> "AnnotationMeta":
        """Merge epics from a Changes instance with epics parsed from an annotation file"""
        for epic in self.epics:
            epic.merge_stories()

        combined = list(
            itertools.chain(
                *[e.epics for e in args],
                self.epics,
            )
        )

        grouped = [
            (k, list(g))
            for k, g in itertools.groupby(
                sorted(combined, key=lambda e: e.name), key=lambda e: e.name
            )
        ]

        merged = {
            name: vorbote.parse.Epic(
                name=name,
                stories=list(itertools.chain(*[e.stories for e in g])),
                description="\n".join(filter(lambda x: x, [e.description for e in g])),
                _impact_class=self._impact_class,
            )
            for name, g in grouped
        }

        # Restore original order & merge stories
        self.epics = [merged[x].merge_stories() for x in [e.name for e in combined]]

        return self

    @property
    def static_fields(self) -> list[str]:
        """Return a list of static annotation elements"""
        return [f.name for f in dataclasses.fields(type(self)) if f.init]

    @property
    def dynamic_fields(self) -> list[str]:
        """Return a list of dynamic/extensible annotation elements"""
        return [f for f in vars(self).keys() if f not in self.static_fields]


@dataclasses.dataclass(init=False, kw_only=True)
class Annotations(AnnotationsMeta, parsers={"epics": Epic}):
    epics: list[Epic]


def get_annotations(
    path: pathlib.Path | str, config: Config, validate: bool = True
) -> Annotations:
    """Get annotations from an annotation YAML file"""
    schema_path = (
        pathlib.Path(__file__).parent.joinpath("schemas").joinpath("annotations.schema")
    )

    with open(pathlib.Path(path), mode="r", encoding="utf-8") as infile:
        data = yaml.load(infile, Loader=yaml.SafeLoader)

    if validate:
        vorbote.schema.validate(path=schema_path, data=data)

    return Annotations(config=config, **data)
