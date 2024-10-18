"""EX05 - `list` Utility Functions"""

__author__ = "730768796"


def only_evens(input: list[int]) -> list[int]:
    evens_list: list[int] = []
    for nums in input:
        if nums % 2 == 0:
            evens_list.append(nums)
    return evens_list


def sub(input: list[int], start: int, end: int) -> list[int]:
    sub_list: list[int] = []
    index: int = start
    while index < end:
        if index == -1:
            index = 0
        if index >= len(input):
            return sub_list
        sub_list.append(input[index])
        index += 1
    return sub_list


def add_at_index(input: list[int], add: int, add_idx: int) -> None:
    if add_idx < 0 or add_idx > len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)
    index: int = len(input) - 1
    while index > add_idx:
        input[index] = input[index - 1]
        index -= 1
    input[add_idx] = add
