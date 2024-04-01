"""Mutating functions."""

__author__ = "730712233"


def manual_append(list1: list[int], num: int) -> None:
    """Adds a number to a list of numbers."""
    list1.append(num)
    return None


def double(list2: list[int]) -> None:
    """Doubles and replaces each number in a list of numbers."""
    index_count: int = 0
    index_max: int = len(list2) - 1
    while index_count <= index_max:
        list2[index_count] *= 2
        index_count += 1
    return None