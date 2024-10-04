"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730768796"


def input_word() -> str:  # function that takes user's inputted word
    word = input("Enter a 5-character word: ")  # word input prompt
    if len(word) == 5:  # checks if word is a 5-character word
        return word
    else:
        print("Error: Word must contain 5 characters.")  # word is not 5-character word
        exit()  # can quit this function now since there is no return in the else


def input_letter() -> str:  # function that takes user's inputted letter
    letter = input("Enter a single character: ")  # letter input prompt
    if len(letter) == 1:  # can only be a single letter
        return letter
    else:
        print(
            "Error: Character must be a single character."
        )  # character is not 1 character
        exit()  # can quit this function now since there is no return in the else


def contains_char(
    word: str, letter: str
) -> None:  # word and letter parameters, no return
    count: int = 0  # counts number of matches of letter in word
    print("Searching for " + letter + " in " + word)
    if letter == word[0]:
        print(letter + " found at index 0")
        count += 1  # keeping track of instances
    if letter == word[1]:
        print(letter + " found at index 1")
        count += 1  # keeping track of instances
    if letter == word[2]:
        print(letter + " found at index 2")
        count += 1  # keeping track of instances
    if letter == word[3]:
        print(letter + " found at index 3")
        count += 1  # keeping track of instances
    if letter == word[4]:
        print(letter + " found at index 4")
        count += 1  # keeping track of instances
    if (
        count > 0 and count != 1
    ):  # final print statement - if instances of letter found in word
        print(str(count) + " instances of " + letter + " found in " + word)
    elif count == 1:  # if 1 instancE of letter is found in word
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(
            "No instances of " + letter + " found in " + word
        )  # if no instances of letter is found in word


def main() -> None:
    contains_char(
        word=input_word(), letter=input_letter()
    )  # main function - putting it all together


if __name__ == "__main__":
    main()  # calling main function
