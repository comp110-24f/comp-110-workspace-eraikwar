"""Dictionaries exercise in COMP110!"""

__author__ = "730768796"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """This function inverts the inputted dictionary."""
    inverted_dict: dict[str, str] = {}  # initializing the dictionary that is returned
    value: str = ""  # store value of each key to replace the existing key with value
    for key in input_dict:  # iterate through dictionary
        value = input_dict[key]  # assign value variable with current value
        if (
            value in inverted_dict
        ):  # if value is already present in the new inverted dictionary, raise key error because they will be repeated
            raise KeyError(
                f"There are two of {value} keys, and there can only be one of each key."
            )
        inverted_dict[value] = key  # invert the stored value and key
    return inverted_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """This function returns the most popular color that appears in the input dictionary."""
    popular_color: str = ""  # initialize popular_color that is returned
    color_frequency: dict[str, int] = (
        {}
    )  # making a new dictionary to store how many times a color appears in the original dictionary
    max: int = 0  # keeping track of the color that appears the most
    for key in input_dict:  # go through the dictionary
        if (
            input_dict[key] in color_frequency
        ):  # if the color is already in the dictionary, add one to the value (count)
            color_frequency[input_dict[key]] += 1
        else:
            color_frequency[input_dict[key]] = (
                1  # if not already in dictionary, add a new color and a value of 1
            )
        if color_frequency[input_dict[key]] > max:  # find the greatest value (count)
            max = color_frequency[input_dict[key]]  # assign it to max
            popular_color = input_dict[key]  # assign key color to popular_color
    return popular_color


def count(input_list: list[str]) -> dict[str, int]:
    """This function takes the input list and returns a dictionary with the items in the list and how many times they appeared in the list."""
    output_dict: dict[str, int] = {}  # initializing the dictionary that is returned
    for elem in input_list:  # go through input list
        if elem in output_dict:  # if item already in list, increase count by 1
            output_dict[elem] += 1
        else:
            output_dict[elem] = 1  # if item not in list, assign count of 1
    return output_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """This function takes the input list and returns a dictionary sorted by the first letter of each word in the list and corresponding values of the words that begin with that letter."""
    output_dict: dict[str, list[str]] = (
        {}
    )  # initializing the dictionary that is returned
    first_letter: str = ""  # store first letter to check all words
    for elem in input_list:  # go through input list
        first_letter = elem[
            0
        ].lower()  # assign first_letter variable the first letter of the current word, lower case!
        if (
            first_letter in output_dict
        ):  # if first_letter is already a key in the dictionary, add the item to the list of the letter
            output_dict[first_letter].append(elem)
        else:
            output_dict[first_letter] = []  # if not already a key, add it
            output_dict[first_letter].append(elem)
    return output_dict


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> None:
    """This function mutates the input dictionary based on the day and student that is inputted to update the attendance."""
    if (day in input_dict) and student not in input_dict[
        day
    ]:  # if day is already in the dictionary, add student to the list of the dictionary
        input_dict[day].append(student)
    else:  # if not in dictionary, make a new list and add it to the value of the day key
        new_students = []
        new_students.append(student)
        input_dict[day] = new_students  # assign new day key to the new students list
