"""EX06 - Dictionary Utility Functions Unit Tests."""

__author__ = "730712233"

from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


def test_invert_string_functionality() -> None:
    """Tests if a dict[str, str] will be properly inverted."""
    input_dict: dict[str, str] = {"sam": "joe"}
    assert invert(input_dict) == {"joe": "sam"}


def test_invert_multiple_key_value_pairs() -> None:
    """Tests if multiple key-value pairings invert properly."""
    input_dict: dict[str, str] = {"sam": "joe", "jaden": "cash"}
    assert invert(input_dict) == {"joe": "sam", "cash": "jaden"}


def test_invert_empty_value_dict() -> None:
    """Tests if an empty value for a key can still be inverted."""
    input_dict: dict[str, str] = {"sam": ""}
    assert invert(input_dict) == {"": "sam"}


def test_count_basic_functionality() -> None:
    """Tests if the elements of a list are correctly counted and collected in a dictionary."""
    input_list: list[str] = ["sam", "jaden", "joe", "cash"]
    assert count(input_list) == {"sam": 1, "jaden": 1, "joe": 1, "cash": 1}


def test_count_multiples() -> None:
    """Tests if recurring items in input list are counted correctly."""
    input_list: list[str] = ["sam", "sam", "joe", "joe", "joe"]
    assert count(input_list) == {"sam": 2, "joe": 3}


def test_count_empty_input_list() -> None:
    """Tests if an empty input list will yield an empty dictionary."""
    input_list: list[str] = []
    assert count(input_list) == {}


def test_favorite_color_basic_functionality() -> None:
    """Tests if the function returns the most common value in the dictionary."""
    input_dict: dict[str, str] = {"sam": "green", "jaden": "green", "joe": "blue", "cash": "red"}
    assert favorite_color(input_dict) == "green"


def test_favorite_color_no_majority() -> None:
    """Tests if the function returns the first color encountered when there is a tie in the count."""
    input_dict: dict[str, str] = {"sam": "green", "joe": "blue"}
    assert favorite_color(input_dict) == "green"


def test_favorite_color_empty_dict() -> None:
    """Tests if an empty string is returned from an empty dictionary."""
    input_dict: dict[str, str] = {}
    assert favorite_color(input_dict) == ""


def test_alphabetizer_basic_functionality() -> None:
    """Tests if a dictionary of letters and the words that begin with them is returned from a list."""
    input_list: list[str] = ["real", "fake", "remain"]
    assert alphabetizer(input_list) == {"r": ["real", "remain"], "f": ["fake"]}


def test_alphabetizer_differing_cases() -> None:
    """Tests if alphabetizer works for words of different cases."""
    input_list: list[str] = ["amazing", "Air", "dog"]
    assert alphabetizer(input_list) != {"a": ["amazing", "air"], "d": ["dog"]}


def test_alphabetizer_number_in_list() -> None:
    """Tests if the correct dictionary is still created when numbers are also in the list."""
    input_list: list[str] = ["joy", "23", "2048"]
    assert alphabetizer(input_list) == {"j": ["joy"], "2": ["23", "2048"]}


def test_update_attendance_add_student_to_existing_day() -> None:
    """Tests if the function adds a student to a day already in the dictionary."""
    input_dict: dict[str, list[str]] = {"monday": ["sam"]}
    assert update_attendance(input_dict, "monday", "joe") == {"monday": ["sam", "joe"]}


def test_update_attendance_add_student_to_new_day() -> None:
    """Tests if the function adds a student to a day not present in the dictionary."""
    input_dict: dict[str, list[str]] = {"monday": ["sam"]}
    assert update_attendance(input_dict, "tuesday", "joe") == {"monday": ["sam"], "tuesday": ["joe"]}


def test_update_attendance_same_name_in_a_day() -> None:
    """Tests if the function repeats the same name in a day."""
    input_dict: dict[str, list[str]] = {"monday": ["sam", "joe"]}
    assert update_attendance(input_dict, "monday", "joe") == {"monday": ["sam", "joe", "joe"]}