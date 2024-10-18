"""Learning list functions."""

__author__ = "730768796"


def get_first(input: list[str]) -> str:
    """Return first element from input list."""
    if len(input) == 0:  # if empty input
        return ""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Removes first element from input list."""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    first_element: str = input[0]
    input.pop(0)
    return first_element
