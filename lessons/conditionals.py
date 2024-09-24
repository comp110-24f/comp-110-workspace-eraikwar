"""Practice with conditionals."""


def less_than_10(num: int) -> None:
    """Tell me if num is < 10."""
    dub: int = num * 2  # example of creating variables
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


less_than_10(num=7)


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger."""
    if hungry is True:  # conditional/boolean expression
        print("Eat some food silly goose!")  # "then" block
    else:
        print("Do your COMP 110 homework instead.")  # "else" block
    print("I'm proud of you <3")  # either way, be kind to yourself.


should_i_eat(hungry=True)


def check_first_letter(word: str, letter: str) -> str:
    """Checks is letter is first character of word."""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter("hi", "i"))


def get_weather_report() -> str:
    """Display weather instructions."""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot"
        print("Keep cool out there!")
    else  
        print("I don't recognize this weather.")
    return weather


get_weather_report()
