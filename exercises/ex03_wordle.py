"""EX03 - Structured Wordle."""

__author__ = "730768796"


def input_guess(secret_word_len: int) -> str:  # input word length of secret word
    """Input a guess with the correct number of characters or try again until it occurs."""
    user_guess = input(f"Enter a {secret_word_len} character word: ")  #
    while len(user_guess) != secret_word_len:  # while it's not correct, try again
        user_guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    print(user_guess)
    return user_guess


# test in REPL through import -- from exercises.ex03_wordle import input_guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Each character is gone through and checked for in the string inputed."""
    assert len(char_guess) == 1  # given -- means assuming char_guess is going to be 1
    idx: int = 0
    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            return True
        idx += 1
    return False


def emojified(guess: str, secret: str):
    """Give emojis like in Wordle to identify which characters belong in the word, which are in the correct place, and which don't belong at all."""
    assert len(guess) == len(
        secret
    )  # given -- means assuming len(guess) is equal to len(secret)
    WHITE_BOX: str = "\U00002B1C"  # white emoji
    GREEN_BOX: str = "\U0001F7E9"  # green emoji
    YELLOW_BOX: str = "\U0001F7E8"  # yellow emoji

    answer: str = ""
    idx: int = 0

    while idx < len(guess):
        if guess[idx] == secret[idx]:  # right letter, right place
            answer += GREEN_BOX
        elif contains_char(secret, guess[idx]):  # right letter, wrong place
            answer += YELLOW_BOX
        else:  # wrong letter, wrong place
            answer += WHITE_BOX
        idx += 1
    return answer


def main(secret: str) -> None:
    """This function takes the input (secret word), keeps track of the user's turns, and determine if the user is a winner if they correctly guess the secret word using the emojis as guides."""
    turns: int = 1  # start at first turn
    winner: bool = False  # did the user win

    while (turns <= 6) and (not winner):  # while not correct guess
        print(f"=== Turn {turns}/{6} ===")
        user_guess: str = input_guess(len(secret))
        answer: str = emojified(user_guess, secret)
        print(answer)
        if user_guess == secret:  # correct guess!!!
            winner = True
        else:
            turns += 1

    if winner:
        print(f"You won in {turns}/6 turns!")
    else:
        print(f"X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main("codes")
