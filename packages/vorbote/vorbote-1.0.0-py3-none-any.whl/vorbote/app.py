import argparse
import datetime
import os.path
import pathlib
import sys

import git
import skabelon

import vorbote.config
from vorbote.annotation import get_annotations
from vorbote.parse import Changes


def parse_date(date: str) -> datetime.date:
    """Parse a date object from an ISO8601 date string"""
    try:
        return datetime.date.fromisoformat(date)
    except ValueError as e:
        raise e


def get_args() -> argparse.Namespace:
    """Parse command-line arguments"""
    today = datetime.date.today()

    _parser = argparse.ArgumentParser()

    _template = _parser.add_mutually_exclusive_group(required=False)

    _template.add_argument(
        "-T",
        "--template-path",
        type=pathlib.Path,
        default=None,
        help="Jinja2 template path (precludes: -t)",
    )

    _template.add_argument(
        "-t",
        "--template-name",
        type=str,
        default="changes.tex.j2",
        help="Jinja2 template name (precludes: -T)",
    )

    _config = _parser.add_argument_group(title="config")

    _config.add_argument(
        "-c",
        "--config",
        "--config-path",
        type=pathlib.Path,
        default=None,
        help="Config file path (default: None)",
    )

    _input = _parser.add_argument_group(title="input")

    _input.add_argument(
        "-s",
        "--schema",
        dest="input_schema",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Toggle JSON schema validation for annotations",
    )

    _input.add_argument(
        "-v",
        "--validate",
        dest="input_validate",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Toggle GIT commit/message validation",
    )

    _output = _parser.add_argument_group(title="output")

    _output.add_argument(
        "-o",
        "--output",
        "--output-path",
        dest="output_path",
        type=pathlib.Path,
        default=None,
        help="Output path (default: None)",
    )

    _output.add_argument(
        "-d",
        "--descriptions",
        dest="output_descriptions",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Toggle showing commit descriptions",
    )

    _output.add_argument(
        "--title",
        dest="output_title",
        type=str,
        default="Change Notes",
        help="Document title (default: 'Change Notes')",
    )

    _output.add_argument(
        "--author",
        dest="output_author",
        type=str,
        default="Vorbote",
        help="Document author (default: 'Vorbote')",
    )

    _output.add_argument(
        "--date",
        dest="output_date",
        type=parse_date,
        default=today,
        help=f"Document author (default: {today.isoformat()}, format: YYYY-MM-DD)",
    )

    _annotation = _parser.add_argument_group(title="annotation")

    _annotation.add_argument(
        "-a",
        "--annotation",
        "--annotation-path",
        dest="annotations",
        type=pathlib.Path,
        action="append",
        help="Annotation YAML path(s) (default: [])",
    )

    _repository = _parser.add_argument_group(title="repository")

    _repository.add_argument(
        "-r",
        "--revision",
        "--revision-range",
        dest="repository_revision",
        type=str,
        default=None,
        help="Git revision range",
    )

    _repository.add_argument(
        "-R",
        "--repository",
        "--repository-path",
        dest="repository_path",
        type=pathlib.Path,
        default="",
        help="Git repository path (default: '.')",
    )

    _project = _parser.add_argument_group(title="project")

    _project.add_argument(
        "-P",
        "--project",
        dest="project_keys",
        action="extend",
        nargs="+",
        help="Project keys (default: [])",
    )

    _tags = _parser.add_argument_group(title="tags")

    _tags.add_argument(
        "--sorted-tag",
        dest="tags_sorted",
        type=str,
        action="append",
        help="Tag(s) honouring input order (default: [])",
    )

    _tags.add_argument(
        "--tag",
        dest="tags_unsorted",
        type=str,
        action="append",
        help="Tag discarding input order (default: [])",
    )

    _exclude = _parser.add_argument_group(title="exclude")

    _exclude.add_argument(
        "-b",
        "--exclude-bare",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Toggle exclusion of bare commits",
    )

    _exclude.add_argument(
        "-m",
        "--exclude-merges",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Toggle exclusion of merge commits",
    )

    _whitespace = _parser.add_argument_group(title="whitespace")

    _whitespace.add_argument(
        "-S",
        "--strip-whitespace",
        dest="whitespace_strip",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Toggle stripping preceding whitespace from template blocks",
    )

    _whitespace.add_argument(
        "-W",
        "--trim-whitespace",
        dest="whitespace_trim",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Toggle trimming surrounding whitespace from template blocks",
    )

    return _parser.parse_args()


def main() -> None:
    """Render a GIT revision range into a predefined Jinja2 template"""
    config = vorbote.config.Config.from_args(args=get_args())

    if config.config:
        file_config = vorbote.config.Config.from_file(path=config.config, validate=True)
        config = config.merge(config=file_config)

    repository = git.Repo(path=config.repository.path)
    commits = repository.iter_commits(rev=config.repository.revision)

    # Gather GIT commits/changes
    changes = Changes.from_commits(
        commits=commits,
        config=config,
    )

    if config.input.validate:
        changes.validate()

    # Gather/merge annotations
    if config.annotations:
        annotations = [
            get_annotations(path=p, config=config, validate=config.input.schema)
            for p in config.annotations
        ]

        changes = annotations[0].merge(*annotations[1:], changes)

    # Initialise Jinja2 template environment
    if config.template.path:
        template_path, template_name = os.path.split(config.template.path.resolve())
    else:
        template_path = pathlib.Path(__file__).parent.joinpath("templates")
        template_name = config.template.name

    environment = skabelon.get_template_environment(
        path=template_path,
        custom_filter_modules=["vorbote.filter"],
        lstrip_blocks=config.whitespace.strip,
        trim_blocks=config.whitespace.trim,
    )

    template = environment.get_template(name=template_name)

    # Render final output from Jinja2 template
    rendered = template.render(
        changes=changes,
        title=config.output.title,
        author=config.output.author,
        date=config.output.date,
        show_descriptions=config.output.descriptions,
        tag_names=[x.name for x in [*config.tags.unsorted, *config.tags.sorted]],
    )

    if config.output.path:
        with open(
            pathlib.Path(config.output.path), mode="w", encoding="utf-8"
        ) as outfile:
            outfile.write(rendered)
    else:
        sys.stdout.write(rendered)


if __name__ == "__main__":
    main()
