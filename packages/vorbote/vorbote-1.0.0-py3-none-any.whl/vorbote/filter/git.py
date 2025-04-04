from vorbote.parse import Author, Message


def format_author(value: Author) -> str:
    """Format author information as `<Name> (<email>)`"""
    return f"{value.name} ({value.email})"


def format_message(value: Message) -> str:
    """Format message tagline"""
    return value.tagline
