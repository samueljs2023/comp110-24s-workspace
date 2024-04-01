"""Splitting a dictionary into two lists."""

__author__ = "730712233"


def get_keys(input: dict[str, int]) -> list[str]:
    """Adds all keys in a dictionary to a list."""
    new_list: list[str] = []
    for key in input:
        new_list.append(key)
    return new_list


def get_values(input: dict[str, int]) -> list[int]:
    """Adds all values in a dictionary to a list."""
    new_list: list[int] = []
    for key in input:
        new_list.append(input[key])
    return new_list