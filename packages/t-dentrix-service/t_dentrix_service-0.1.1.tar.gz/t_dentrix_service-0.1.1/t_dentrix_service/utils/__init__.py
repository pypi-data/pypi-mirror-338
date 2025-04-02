"""Utils."""

import re


def clean_name(name: str) -> str:
    """Clean the name by removing non-alphanumeric characters and converting to lowercase."""
    return re.sub(r"\W+", "", name).lower() if name else ""
