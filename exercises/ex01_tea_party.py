"""This program will tell me how many tea bags and treats I need, along with how much the tea party will cost when a number of guests is inputted!"""  # number of guests is inputted by the user, output is number of guests, tea bags, treats, and total cost.

__author__ = "730768796"  # PID Number


def main_planner(guests: int) -> None:  # blueprint function
    """Print the output and serve as a big picture."""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # convert number of guests (int) to str in order to print
    print(
        "Tea Bags: " + str(tea_bags(guests))
    )  # convert number of tea bags (int) to str in order to print
    print(
        "Treats: " + str(treats(guests))
    )  # convert number of treats (int) to str in order to print
    print(
        "Cost: $" + str(cost(tea_bags(guests), treats(guests)))
    )  # convert number of tea bags and treats (int) to str in order to print


def tea_bags(
    people: int,
) -> (
    int
):  # need to call this function in other functions, each person gets two tea bags.
    """Return the number of tea bags needed if each person uses two."""
    return people * 2


def treats(
    people: int,
) -> (
    int
):  # need to call this function in other functions, each tea bag means 1.5 treats.
    """Return the number of treats needed if for each tea, guests need 1.5 treats."""
    return int(tea_bags(people=people) * 1.5)  # convert float to int


def cost(tea_count: int, treat_count: int) -> float:
    """Return the total cost of tea bags and treats combined if tea bags cost $0.50 each and treats cost $0.75 each"""
    return (tea_count * 0.5) + (treat_count * 0.75)  # don't need to convert to int.


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party? "))
    )  # users can now input value for number of guests.
