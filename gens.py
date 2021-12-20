nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(my_list):
    cursor = 0
    sub_cursor = 0
    while cursor < len(my_list):
        if sub_cursor < len(my_list[cursor]):
            yield my_list[cursor][sub_cursor]
            sub_cursor += 1
        elif cursor + 1 != len(my_list):
            sub_cursor = 0
            cursor += 1
            yield my_list[cursor][sub_cursor]
            sub_cursor += 1
        else:
            break


for item in flat_generator(nested_list):
    print(item)

