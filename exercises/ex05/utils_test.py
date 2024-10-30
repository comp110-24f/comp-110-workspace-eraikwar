"""This tests the functionality of utils.py."""

__author__ = "730768796"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_return_value() -> None:
    """only_evens should return a list of all the even integers in the input list."""
    list_1: list[int] = [11, 2, 5, 4, 4, 4]  # list for testing
    assert only_evens(list_1) == [
        2,
        4,
        4,
        4,
    ]  # these are the even integers in the list above


def test_only_evens_behavior() -> None:
    """only_evens should not mutate the input list."""
    list_1: list[int] = [11, 2, 5, 4, 4, 4]  # list for testing
    only_evens(list_1)
    assert list_1 == [11, 2, 5, 4, 4, 4]  # the list should remain the same


def test_only_evens_edge_case() -> None:
    """only_evens called on an empty list should return an empty list []."""
    assert only_evens([]) == []  # list should be empty


def test_sub_return_value() -> None:
    """sub should return a list of all the elements in between the start and end index that is inputted by the user."""
    list_1: list[int] = [11, 22, 33, 44, 55]  # list for testing
    assert sub(list_1, 1, 4) == [
        22,
        33,
        44,
    ]  # the sub_list should only consist of these values


def test_sub_behavior() -> None:
    """sub should not mutatate the input list."""
    list_1: list[int] = [11, 22, 33, 44, 55]  # list for testing
    sub(list_1, 1, 4)
    assert list_1 == [11, 22, 33, 44, 55]  # list should remain the same


def test_sub_edge_case() -> None:
    """sub with a negative start index should start at the beginning of the list."""
    list_1: list[int] = [11, 22, 33, 44, 55]  # list for testing
    assert sub(list_1, -1, 3) == [
        11,
        22,
        33,
    ]  # having a - start index should start the input list at the beginning


def test_add_at_index_return_value() -> None:
    """add_at_index should return nothing."""
    list_1: list[int] = [101, 202, 303, 505]  # list for testing
    assert add_at_index(list_1, 4, 3) == None  # no return value


def test_add_at_index_behavior() -> None:
    """add_at_index should add a number to the selected index to the input list."""
    list_1: list[int] = [101, 202, 303, 505]  # list for testing
    add_at_index(list_1, 404, 3)
    assert list_1 == [
        101,
        202,
        303,
        404,
        505,
    ]  # the list should have added 404 at index 3


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    list_1: list[int] = [101, 202, 303, 505]  # list for testing
    with pytest.raises(IndexError):
        add_at_index(list_1, 606, 6)
        # an IndexError is raised for the case when the add_at_index is given an index that is greater than the length of our input list
