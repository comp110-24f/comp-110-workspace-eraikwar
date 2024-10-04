"""Virtual lesson about scopes on 9/25/24."""

__author__ = "730768796"


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""  # Set up empty str to copy values over
    index: int = (
        0  # local variable: copy, index, msg, char -- can only be accessed inside the function
    )
    # print(word)
    while index < len(msg):
        if (
            msg[index] != char
        ):  # if the letter is not char or if not (msg[index] == char):
            copy += msg[index]  # add it to copy string
        index += 1
    return copy


if __name__ == "__main__":  # the name is gonna be main only if file is running directly
    # create a variable called word with value "yoyo"
    word: str = "yoyo"  # global variable
    # Print the result of calling your function with arguments word and “y”
    print(remove_chars(word, "y"))  # with keyword arguments
    # print the result of calling your function with arguments word and “o”
    # print(remove_chars(word, "o"))  # with positional arguments from below!
    # Challenge: try using positional arguments if you can!
    # print(remove_chars("football", "o"))
