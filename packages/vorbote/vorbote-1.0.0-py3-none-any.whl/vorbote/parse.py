import dataclasses
import datetime
import functools
import itertools
import re
import uuid
from typing import Any, Callable, Iterator, get_origin, Type

from git import Commit

from vorbote.config import Config, Tag


@dataclasses.dataclass
class Validator:
    test: Callable
    message: str
    data: Any | list[Any] = None

    def validate(self) -> None:
        """Check if a validation test passes, otherwise throw an Assertion error"""
        assert self.test(self.data), (
            f"{self.message}, data={self.data}" if self.data else self.message
        )


@dataclasses.dataclass
class Author:
    name: str
    email: str

    @classmethod
    def from_commit(cls, commit: Commit) -> "Author":
        """Parse an author from a GIT commit"""
        _author = commit.author

        return cls(name=_author.name, email=_author.email)

    @property
    def key(self) -> str:
        """Return a unique identifier for an author"""
        return self.email

    def __hash__(self) -> int:  # pragma: no cover
        return hash(self.key)

    def __eq__(self, other: Any) -> bool:  # pragma: no cover
        return self.key == other

    def __lt__(self, other: Any) -> bool:  # pragma: no cover
        return self.key < other

    def __gt__(self, other: Any) -> bool:  # pragma: no cover
        return self.key > other


@dataclasses.dataclass
class Impact:
    def __post_init__(self):
        for f in dataclasses.fields(self):
            if get_origin(f.type) == list and getattr(self, f.name) == [""]:
                setattr(self, f.name, [])

    @classmethod
    def factory(
        cls, fields: list[tuple[str, Type] | tuple[str, Type, dataclasses.Field]]
    ) -> Type["Impact"] | type:
        _fields = [
            (*x, dataclasses.field(default_factory=list)) if len(x) == 2 else x
            for x in fields
        ]

        _dataclass = dataclasses.make_dataclass("Impact", fields=_fields, bases=(cls,))

        return _dataclass

    @classmethod
    def from_config(cls, config: Config) -> Type["Impact"] | type:
        tags_unsorted: list[Tag] = config.get("tags", "unsorted") or []
        tags_sorted: list[Tag] = config.get("tags", "sorted") or []

        tags = [*tags_unsorted, *tags_sorted]

        return cls.factory(fields=[x.to_field() for x in tags])

    @classmethod
    def from_commit(cls, commit: Commit) -> "Impact":
        """Retrieve impact fields from GIT commit trailers"""
        _trailers = dict(commit.trailers_list)

        inline_regex = re.compile(r",\s?")
        nested_regex = re.compile(r"\s*\+\s*")

        kwargs = {}

        for f in dataclasses.fields(cls):
            _value = _trailers.get(f.name, "")

            if not _value:
                kwargs[f.name] = []
            elif nested_regex.search(_value):
                kwargs[f.name] = [x for x in nested_regex.split(_value) if x]
            elif inline_regex.search(_value):
                kwargs[f.name] = [x for x in inline_regex.split(_value) if x]
            else:
                kwargs[f.name] = [_value]

        return cls(**{k: v for k, v in kwargs.items() if v != [""]})

    @classmethod
    def merge(cls, impacts: list["Impact"]) -> "Impact":
        """Combine any number of Impact instances into a new, single instance"""
        kwargs = {}

        for f in dataclasses.fields(cls):
            values = itertools.chain(*[getattr(x, f.name) for x in impacts])

            kwargs[f.name] = (
                list(values) if f.metadata.get("sorted", False) else sorted(set(values))
            )

        return cls(**kwargs)

    @property
    def empty(self) -> bool:
        """Return whether any impact values are present"""
        return not any(vars(self).values())


@dataclasses.dataclass
class Ticket:
    key: str | None = None
    id: str | None = None

    @classmethod
    def from_message(cls, message: str, regex: re.Pattern) -> "Ticket":
        """Parse a potential ticket reference from a given message"""
        _match = regex.match(message)

        if isinstance(_match, re.Match):
            kwargs = dict(
                zip([f.name for f in dataclasses.fields(cls)], _match.groups())
            )
        else:
            kwargs = {}

        return cls(**kwargs)

    @classmethod
    def from_reference(cls, reference: str) -> "Ticket":
        """Parse a ticket reference from a reference string"""
        return cls(*reference.split("-"))

    @property
    def reference(self) -> str | None:
        """Return a formatted ticket reference"""
        return f"{self.key}-{self.id}" if all([self.key, self.id]) else None

    def __hash__(self) -> int:
        return hash(self.reference)

    def __eq__(self, other: Any) -> bool:
        return self.reference == other

    def __lt__(self, other: Any) -> bool:
        return self.reference < other

    def __gt__(self, other: Any) -> bool:
        return self.reference > other


@dataclasses.dataclass
class Message:
    tagline: str
    descriptions: list[str]
    impact: Impact
    epic: str | None
    ticket: Ticket | None
    sha: str
    author: Author | None
    timestamp: datetime.datetime | None
    __qualified: bool = dataclasses.field(init=False)

    @classmethod
    def from_commit(cls, commit: Commit, config: Config):
        """Parse GIT commit object into class instance"""
        project_keys = config.project.keys or [r"[A-Za-z]+"]

        _impact_class = Impact.from_config(config=config)

        _message = list(
            filter(lambda x: x, cls.clean_message(commit.message).split("\n"))
        )

        _tagline = _message[0]
        _fields = [*dataclasses.fields(_impact_class), *dataclasses.fields(cls)]

        trailer_regex = re.compile(
            rf"^({'|'.join([x.name for x in _fields])}:\s+|\s+\+\s?)"
        )
        ticket_regex = re.compile(
            rf"(?i)^(?P<key>{'|'.join(project_keys)})-(?P<id>\d+)(:?\s+)(?P<msg>.+)"
        )

        __qualified = isinstance(ticket_regex.match(_tagline), re.Match)

        if __qualified:
            tagline = ticket_regex.match(_tagline).group("msg")
        else:
            tagline = _tagline

        _class = cls(
            tagline=tagline,
            descriptions=[x for x in _message[1:] if not trailer_regex.match(x)],
            impact=_impact_class.from_commit(commit=commit),
            ticket=Ticket.from_message(message=_tagline, regex=ticket_regex),
            epic=dict(commit.trailers_list).get("epic", None),
            sha=commit.hexsha,
            author=Author.from_commit(commit=commit),
            timestamp=commit.committed_datetime,
        )
        _class.__qualified = __qualified

        return _class

    @property
    def qualified(self) -> bool:
        """Return whether the current message contains a ticket reference"""
        return self.__qualified

    @qualified.setter
    def qualified(self, value: bool) -> None:
        self.__qualified = value

    @property
    def bare(self) -> bool:
        """Return whether the current message contains no ticket reference"""
        return not self.__qualified

    @property
    def merge(self) -> bool:
        """Return whether the current message marks a merge commit"""
        tests = [
            "Merge pull request #",
            "Merge branch '",
            "Merge remote-tracking branch '",
        ]

        return any([t in self.tagline for t in tests])

    @staticmethod
    def clean_message(message: str) -> str:
        """Clean commit messages to ensure proper rendering"""
        functions = [
            lambda x: x.replace("\r", ""),
            lambda x: re.sub(r"(\s*)\*", r"\1-", x),
        ]

        return functools.reduce(lambda a, b: b(a), functions, message)


@dataclasses.dataclass
class Story:
    ticket: Ticket
    messages: list[Message]
    _impact_class: Type[Impact] = dataclasses.field(default_factory=Impact)

    @functools.cached_property
    def key(self) -> str:
        """Return a unique identifier for a story"""
        return self.ticket.reference or f"Dummy({uuid.uuid4().hex})"

    @functools.cached_property
    def impact(self) -> Impact:
        """Gather all subordinate impacts into a single Impact instance"""
        return self._impact_class.merge(impacts=[x.impact for x in self.messages])

    @functools.cached_property
    def authors(self) -> list[Author]:
        """Gather all subordinate authors"""
        return sorted({x.author for x in self.messages})

    @functools.cached_property
    def hashes(self) -> list[str]:
        """Gather all subordinate commit hashes"""
        return [x.sha for x in self.messages]

    def __hash__(self) -> int:
        return hash(self.key)

    def __eq__(self, other: Any) -> bool:
        return self.key == other

    def __lt__(self, other: Any) -> bool:
        return self.key < other

    def __gt__(self, other: Any) -> bool:
        return self.key > other

    def __str__(self) -> str:
        return self.key


@dataclasses.dataclass
class Epic:
    name: str
    stories: list[Story] = dataclasses.field(default_factory=list)
    description: str | None = None
    _impact_class: Type[Impact] = dataclasses.field(default_factory=Impact)

    def __post_init__(self):
        if isinstance(self.description, str):
            self.description = self.description.strip()

    @functools.cached_property
    def key(self) -> str:
        """Transform a free-form epic name into a consistent snake_cased key"""
        return re.sub(r"_$", "", re.sub(r"\W+", "_", self.name)).lower()

    @functools.cached_property
    def impact(self) -> Impact:
        """Gather all subordinate impacts into a single Impact instance"""
        return self._impact_class.merge(impacts=[x.impact for x in self.stories])

    @functools.cached_property
    def authors(self) -> list[Author]:
        """Gather all subordinate authors"""
        return sorted(set.union(*[set(x.authors) for x in self.stories]))

    @functools.cached_property
    def hashes(self) -> list[str]:
        """Gather all subordinate commit hashes"""
        return list(itertools.chain(*[x.hashes for x in self.stories]))

    @functools.cached_property
    def tickets(self) -> list[str]:
        """Gather all subordinate tickets"""
        return [x.ticket.reference for x in self.stories]

    def merge_stories(self) -> "Epic":
        """Merge subordinate stories in case story names exist more than once"""
        _stories = {}

        for story in self.stories:
            if story in _stories:
                parent = _stories.get(story)
                parent.messages = [*parent.messages, *story.messages]
            else:
                _stories[story] = story

        self.stories = list(_stories.values())

        return self

    def __str__(self) -> str:
        return self.name


@dataclasses.dataclass
class Changes:
    messages: list[Message]
    _impact_class: Type[Impact] = dataclasses.field(default_factory=Impact)
    __unassigned: str = dataclasses.field(init=False, default="Unassigned")

    @classmethod
    def from_commits(
        cls,
        commits: list[Commit] | Iterator[Commit],
        config: Config,
    ) -> "Changes":
        """Parse (and optionally filter) a list of git commits into Message instances"""
        _messages = [
            Message.from_commit(commit=commit, config=config) for commit in commits
        ]

        if config.exclude.bare:
            _messages = cls.filter_exclude_bare(messages=_messages)

        if config.exclude.merges:
            _messages = cls.filter_exclude_merges(messages=_messages)

        return cls(messages=_messages, _impact_class=Impact.from_config(config=config))

    def group_messages(self) -> dict[str, dict[Ticket, list[Message]]]:
        """Group messages into a hierarchy (epic > story > commit)"""
        epics = {}
        tickets = {}
        group = []

        # Group messages by ticket
        for m in reversed(self.messages):
            if m.qualified:
                tickets[m.ticket] = list(
                    reversed([*tickets.get(m.ticket, []), *group, m])
                )
                group = []
            else:
                group.append(m)

        # Merge/backfill epics if only some commits for the same story contain an epic
        parsed_epics = {
            k: ({m.epic for m in v if m.epic} or {None}).pop()
            for k, v in tickets.items()
        }

        for k, v in tickets.items():
            for message in v:
                message.epic = message.epic or parsed_epics.get(k, None)

        # Combine tickets by epic
        for m in reversed(self.messages):
            if m.qualified:
                _epic = m.epic or self.__unassigned

                epics[_epic] = {**epics.get(_epic, {}), m.ticket: tickets[m.ticket]}

        # Combine any leftovers into the default/unassigned epic
        if group:
            epics[self.__unassigned] = {
                **epics.get(self.__unassigned, {}),
                Ticket(): group,
            }

        return epics

    def validate(self) -> "Changes":
        """Assert that all commits belong to valid trees of Epics/Stories"""
        tests = [
            Validator(
                test=lambda _: len(self.messages) > 0,
                message="No commits found",
            ),
            Validator(
                test=lambda _: len([m for m in self.messages if m.qualified]) > 0,
                message="No qualified commits found",
            ),
            Validator(
                data=(
                    self._default_epic.hashes
                    if self._default_epic.hashes and not any(self._default_epic.tickets)
                    else None
                ),
                test=lambda x: x is None,
                message="Found dangling unqualified commits",
            ),
            Validator(
                data=self._default_epic.hashes,
                test=lambda x: len(x) == 0,
                message="Found commits without assigned epic",
            ),
        ]

        for test in tests:
            test.validate()

        return self

    @functools.cached_property
    def epics(self) -> list[Epic]:
        """Return a list of Epics (with their subordinate stories etc.)"""
        _epics = [
            Epic(
                name=epic,
                stories=[
                    Story(ticket=t, messages=m, _impact_class=self._impact_class)
                    for t, m in tickets.items()
                ],
                _impact_class=self._impact_class,
            )
            for epic, tickets in self.group_messages().items()
        ]

        return _epics

    @functools.cached_property
    def _default_epic(self) -> Epic:
        """Return default epic (which gathers all stories without associated epic)"""
        _default = [x for x in self.epics if x.name == self.__unassigned]

        return _default[0] if _default else Epic(name=self.__unassigned)

    @staticmethod
    def filter_exclude_bare(messages: list[Message]) -> list[Message]:
        """Exclude any messages that do not contain a ticket number"""
        return list(filter(lambda m: not m.bare, messages))

    @staticmethod
    def filter_exclude_merges(messages: list[Message]) -> list[Message]:
        """Exclude any messages that contain a merge (branch or pull request)"""
        return list(filter(lambda m: not m.merge, messages))
