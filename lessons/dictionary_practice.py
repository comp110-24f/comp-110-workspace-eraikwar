"""Splitting a dictionary into two lists."""

__author__ = "730768796"


def get_keys(input_dict: dict[str, int]) -> list[str]:
    """This function should produce a list of all the keys in the input dictionary."""
    if len(input_dict) == 0:  # return empty list if empty dictionary
        return []
    keys_list: list[str] = []  # initialize keys_list to empty list
    for keys in input_dict:
        keys_list.append(keys)  # add keys in input_dict to keys_list
    return keys_list


def get_values(input_dict: dict[str, int]) -> list[int]:
    """This function should produce a list of all the values in the input dictionary."""
    if len(input_dict) == 0:  # return empty list if empty dictionary
        return []
    values_list: list[int] = []  # initialize values_list to empty list
    for vals in input_dict:
        values_list.append(input_dict[vals])  # add values in input_dict to values_list
    return values_list
