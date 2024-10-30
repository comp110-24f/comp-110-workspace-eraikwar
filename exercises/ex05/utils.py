"""EX05 - `list` Utility Functions"""

__author__ = "730768796"


def only_evens(input: list[int]) -> list[int]:
    """This function returns a list of the even integers in the input list."""
    evens_list: list[int] = []  # initialize list of even integers
    for nums in input:
        if nums % 2 == 0:  # if even
            evens_list.append(nums)  # add to evens)list
    return evens_list


def sub(input: list[int], start: int, end: int) -> list[int]:
    """This function returns a list from the input list with stated start and end indexes."""
    sub_list: list[int] = []  # initialize list of integers
    index: int = start  # start this new list at the given start index
    while index < end:  # go until the specified end index
        if index < 0:  # if negative, start at the beginning of the list
            index = 0
        if index >= len(
            input
        ):  # when the end of the input list has approached, return the sub_list
            return sub_list
        sub_list.append(
            input[index]
        )  # add value to sub_list if by passes all of the if conditions
        index += 1  # go to the next item on the list
    return sub_list


def add_at_index(input: list[int], add: int, add_idx: int) -> None:
    """This function adds values to the input list at the stated index."""
    if add_idx < 0 or add_idx > len(
        input
    ):  # if index is not within list, raise Index Error
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)  # add an extra spot on the list
    index: int = len(input) - 1  # start from the end of the list
    while index > add_idx:
        input[index] = input[index - 1]  # shift value to the right
        index -= 1  # go to the previous value
    input[add_idx] = add  # lastly, add the given add value to the index desired
