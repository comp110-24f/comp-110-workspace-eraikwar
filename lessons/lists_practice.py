"""Basic syntax of lists."""

# Create an empty list of floats called my_numbers
my_numbers: list[float] = []  # literal ex: empty string ""
my_numbers: list[float] = list()  # constructor ex: enpty string str()
my_numbers.append(0.25)
my_numbers.append(0.50)
print(my_numbers)  # prints entire list


def display(int_list: list[int]) -> None:
    """Prints every element in the input list."""
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


game_points: list[int] = [102, 86, 94]  # Creating an already populated list.
print(game_points[2])  # Indexing/Subscription Notation
game_points[1] = 72  # modifying items in a list
game_points.pop(1)  # remove an item using index from list
display(int_list=game_points)  # call function to print entire list

print(game_points)  # prints entire list
print(len(game_points))  # length of lists len(list_name)

# example -- class_num: str = "110"
# class_num[0] = "2"  # modifying items in a list doesn't work for strings!!

# List with multiple types: game_points: list[int | float] = [102, 86, 94, 5.5]
