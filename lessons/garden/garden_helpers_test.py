"""Test my garden functions."""

__author__ = "730712233"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind_empty_dict() -> None:
    """Tests if the function add_by_kind works while the dictionary is empty."""
    test_dict: dict[str, list[str]] = {}
    add_by_kind(test_dict, "flower", "kind")
    assert test_dict == {"flower": ["kind"]}


def test_add_by_kind_indexed_list() -> None:
    """Tests if indexed lists can be used in place of str values as a paramter."""
    test_kind_list: list[str] = ["tree", "flower"]
    test_plant_list: list[str] = ["rose", "pine"]
    test_dict: dict[str, list[str]] = {"type": ["plant"]}
    add_by_kind(test_dict, test_kind_list[1], test_plant_list[0])
    assert test_dict == {"type": ["plant"], "flower": ["rose"]}


def test_add_by_date_first_new_date() -> None:
    """Tests if function adds a new plant to an existing list properly."""
    test_dict: dict[str, list[str]] = {"month": ["plant"]}
    add_by_date(test_dict, "month", "rose")
    assert test_dict == {"month": ["plant", "rose"]}


def test_add_by_date_empty_str() -> None:
    """Tests if inputting empty strings changes nothing in the dictionary."""
    test_dict: dict[str, list[str]] = {"month": ["plant"]}
    add_by_date(test_dict, "", "")
    assert test_dict == {"month": ["plant"]}


def test_lookup_by_kind_and_date_empty_combined_list() -> None:
    """Tests the function output when the combined list is empty."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["rose"], "tree": ["pine"]}
    plants_by_date: dict[str, list[str]] = {"may": ["strawberry"], "june": ["grass"]}
    assert lookup_by_kind_and_date(plants_by_kind, plants_by_date, "tree", "may") == "No trees to plant in may."


def test_lookup_by_kind_and_date_repeated_terms() -> None:
    """Tests if repeated plants in lists are still returned."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["rose", "rose"]}
    plants_by_date: dict[str, list[str]] = {"may": ["strawberry", "rose"]}
    assert lookup_by_kind_and_date(plants_by_kind, plants_by_date, "flower", "may") == "flowers to plant in may: ['Rose']"