"""My first challenge question in COMP110!"""

__author__ = "730768796"


def mimic(message: str) -> str:
    """A function that mimics what you input."""
    return message


def main() -> None:
    """A function that pulls together all functions."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
