"""This tests the functionality of find_max."""

__author__ = "730768796"

from CQs.cq07.find_max import find_and_remove_max


# return value test
def test_find_and_remove_max_return_value() -> None:
    """find_and_remove_max should return the largest integer in the list."""
    nums_input: list[int] = [5, 30, 2, 65, 81, 22, 100, 100]
    assert find_and_remove_max(nums_input) == 100  # return value should be 100


# desired behavior test to see what changes it makes to the list itself
def test_find_and_remove_max_behavior() -> None:
    """find_and_remove_max should remove the largest integer from the input list."""
    nums_input: list[int] = [5, 30, 2, 65, 81, 22, 100, 100]
    find_and_remove_max(nums_input)
    assert nums_input == [5, 30, 2, 65, 81, 22]


# edge case to test what it does with an empty list
def test_get_first_edge_case() -> None:
    """find_and_remove_max called on an empty list should return -1."""  # this is what i want it to do.
    nums_input: list[int] = []
    assert find_and_remove_max(nums_input) == -1
