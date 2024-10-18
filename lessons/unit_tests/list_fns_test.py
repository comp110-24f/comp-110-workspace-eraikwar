from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    """get_first should return first element."""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert get_first(dog_breeds) == "husky"  # return value should be "husky"


# desired return value
def test_remove_first_return_value() -> None:
    """remove_first should return nothing."""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert remove_first(dog_breeds) == None


# desired behavior
def test_remove_first_behavior() -> None:
    """remove_first should remove the first element from the input list."""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    remove_first(dog_breeds)
    assert dog_breeds == ["golden", "poodle", "lab"]


# use case: how we expect program to be used
# edge case: outside "typical" usage, ex- empty inputs, incorrect inputs, etc.


def test_get_first_edge_case() -> None:
    """get_first called on an empty list should return an empty string ("")."""  # this is what i want it to do.
    assert get_first([]) == ""
