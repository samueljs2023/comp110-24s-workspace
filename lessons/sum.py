"""Summing the elements of a list using different loops."""

__author__ = "730712233"


def w_sum(vals: list[float]) -> float:
    """Sums floats in a list using a while loop."""
    w_sum_counter: int = 1
    result: float = 0.0
    if len(vals) == 0:
        result == 0.0
    else:
        while w_sum_counter <= len(vals):
            result += vals[w_sum_counter - 1]
            w_sum_counter += 1
    return result


def f_sum(vals: list[float]) -> float:
    """Sums floats in a list using a for loop only."""
    result: float = 0.0
    for elem in vals:
        result += elem
    return result


def f_range_sum(vals: list[float]) -> float:
    """Sums floats in a list using the range function and a for loop."""
    result: float = 0.0
    x: int = len(vals)
    for idx in range(0, x, 1):
        result += vals[idx]
    return result