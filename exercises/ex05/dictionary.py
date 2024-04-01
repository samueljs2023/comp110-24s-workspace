"""EX05 - Dictionary Utility Functions."""

__author__ = "730712233"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Makes the keys of the input list the values of the output list and vice versa."""
    output_dict: dict[str, str] = {}
    input_keys: list[str] = []
    input_values: list[str] = []
    counter: int = 0
    error_counter: int = 0
    for key in input_dict:
        input_keys.append(key)
        input_values.append(input_dict[key])
    while error_counter < len(input_dict):
        for x in range(error_counter + 1, len(input_dict)):
            if input_values[error_counter] == input_values[x]:
                raise KeyError("Keys must be unique.")
        error_counter += 1
    while counter < len(input_dict):
        output_dict[input_values[counter]] = input_keys[counter]
        counter += 1
    return output_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    new_dict: dict[str, int] = {}
    for elem in input_dict:
        if input_dict[elem] in new_dict:
            new_dict[input_dict[elem]] += 1
        else:
            new_dict[input_dict[elem]] = 1
    favorite: str = ""
    favorite_counter: int = 0
    for elem in new_dict:
        if new_dict[elem] > favorite_counter:
            favorite_counter = new_dict[elem]
            favorite = elem
    return favorite
    
    
def count(input: list[str]) -> dict[str, int]:
    """Creates a dictionary counting each item on the list."""
    output: dict[str, int] = {}
    for elem in input:
        if elem in output:
            output[elem] += 1
        else:
            output[elem] = 1
    return output


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Compiles a dictionary of letters, and all words that begin with that letter from a list."""
    lower_case_list: list[str] = []
    output: dict[str, list[str]] = {}
    for elem in input:
        lower_case_list.append(elem.lower())
    for elem in lower_case_list:
        if elem[0] not in output:
            output[elem[0]] = [elem]
        else:
            output[elem[0]].append(elem)
    return output


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Mutates the input dictionary by updating the input attendance information."""
    if day in input_dict:
        if student not in input_dict:
            input_dict[day].append(student)
    else:
        input_dict[day] = [student]
    return None