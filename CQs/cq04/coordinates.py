"""Part 3 of CQ04!"""

__author__ = "730768796"


def get_coords(xs: str, ys: str) -> None:
    index_xs: int = 0
    while index_xs < len(xs):
        index_ys: int = 0
        while index_ys < len(ys):
            print("(" + xs[index_xs] + "," + ys[index_ys] + ")")
            index_ys += 1
        index_xs += 1


get_coords("hi", "bye")
