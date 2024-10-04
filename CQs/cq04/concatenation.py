"""Part 1 of CQ04!"""

__author__ = "730768796"


def concat(part1: str, part2: str) -> str:
    """Returns the concatenation of the two input strings."""
    concatenated_word: str = part1 + part2
    return concatenated_word


word1: str = "happy"
word2: str = "tuesday"
if __name__ == "__main__":
    print(concat(word1, word2))
