nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]]


class FlatIterator:
    def __init__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        self.cursor = 0
        self.sub_cursor = -1
        return self

    def __next__(self):
        if self.sub_cursor + 1 < len(self.my_list[self.cursor]):
            self.sub_cursor += 1
        elif self.cursor + 1 < len(self.my_list):
            self.cursor += 1
            self.sub_cursor = 0
        else:
            raise StopIteration
        return self.my_list[self.cursor][self.sub_cursor]


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
