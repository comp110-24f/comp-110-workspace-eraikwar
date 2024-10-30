"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

ice_cream["vanilla"] += 110

# len evaluates to the number of entries
print(len(ice_cream))

# add key-value entry by directly assigning to a key
ice_cream["mint"] = 3

# access entries by their keys
print(ice_cream["chocolate"])  # prints 12

# test if "PBJ" is a key in ice_cream
has_pbj: bool = "pbj" in ice_cream

# to remove, use pop method and give a key
ice_cream.pop("strawberry")  # returns value associated with key popped

# to iterate over every key in a loop, use for..in loop
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} orders.")
