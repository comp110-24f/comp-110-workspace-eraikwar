"""EX03 - list Utility Functions."""

__author__ = "730768796"


def all(int_list: list[int], num: int) -> bool:
    """Checking if all the ints in the list are the same as the given int."""
    for nums in int_list:  # goes through each value in list
        if nums == num:  # checks if equal to int
            return True
        else:
            return False  # if not, False is returned.
    return False


def max(int_list: list[int]) -> int:
    """Should return largest int in list."""
    if len(int_list) == 0:  # given. raises value error is an empty list is inputted.
        raise ValueError("max() arg is an empty List")
    max_num: int = int_list[0]  # start with the first number in the list.
    for num in int_list:  # goes through each value in the list
        if num > max_num:  # checks if value is greater than the recorded max_num
            max_num = num  # if so, replaces max_num
    return max_num


def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    """Checks if each value in the two lists are equal."""
    if len(int_list1) == len(int_list2):
        index: int = 0
        while index < len(int_list1):  # checks two lists
            if (
                int_list1[index] == int_list2[index]
            ):  # both lists at the same index are checked.
                index += 1
            else:
                return False
        return True
    return False


def extend(int_list1: list[int], int_list2: list[int]) -> None:
    """Add the second list's values to the first list."""
    for nums in int_list2:  # goes through each value in second list
        int_list1.append(nums)  # adds values from second list to first list
