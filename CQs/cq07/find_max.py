"""This functions finds the maximum int in a list and removes it."""

__author__ = "730768796"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:  # edge case: empty list
        return -1

    max: int = input[0]  # maximum integer value
    for idx in range(0, len(input)):  # go through input list using range
        if (
            input[idx] > max
        ):  # if value at given index is more than max, replace max value
            max = input[idx]
    index: int = 0
    while index < len(input):  # go through list
        if (
            max == input[index]
        ):  # if there are multiple of the same max value, remove it from list.
            input.pop(index)
        else:
            index += 1
    return max
