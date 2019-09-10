def get_statement(bottle_count):
    holder_str = "Take one down and pass it around, " if (
                bottle_count - 1 >= 0) else "Go to the store and buy some more, "

    return get_bottle_str(bottle_count) + " of beer on the wall, " + get_bottle_str(
        bottle_count) + " of beer\n" + holder_str + get_bottle_str(
        bottle_count - 1) + " of beer on the wall.\n"


def get_bottle_str(bottle_count):
    bottle_count = bottle_count if bottle_count >= 0 else 100 + bottle_count  # handle for < 0
    count_str = str(bottle_count) if bottle_count > 0 else "no more"  # handle for 0
    return (count_str + " bottles") if (bottle_count > 1) else (count_str + " bottle")  # handle for 1


for i in range(99, -1, -1):
    print(get_statement(i))
