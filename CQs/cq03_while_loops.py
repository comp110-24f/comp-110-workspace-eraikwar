"""My third challenge question in COMP110 with while loops!"""

__author__ = "730768796"


def num_instances(
    phrase: str, search_char: str
) -> int:  # two string parameters, returns int for count
    count: int = 0  # number of times character is in word
    index: int = 0  # helps traverse through each character in phrase
    while index < len(
        phrase
    ):  # boolean condition that will eventually be false, so no infinite loop
        if (
            phrase[index] == search_char
        ):  # boolean condition - if character is in phrase, add to count
            count = count + 1
        index = index + 1  # go to next letter in phrase
    return count  # after exiting the while loop, return count of character in phrase
