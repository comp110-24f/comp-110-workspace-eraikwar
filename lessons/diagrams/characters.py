def characters(msg: str) -> None:
    index: int = 0
    while index < len(
        msg
    ):  # condition has to eventually be false otherwise this will be an infinite loop (press Ctrl C to stop it.)
        print(msg[index])
        index = index + 1


characters(msg="Howdy")
