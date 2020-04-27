import math
import random

import timy


class MyObject:
    def __init__(self, x):
        self.x = x

    def do_it(self):
        return math.sqrt(self.x) + self.x ** self.x


@timy.timer(loops=1000)
def with_map(input_data):
    return map(lambda foo: foo.do_it(), input_data)


@timy.timer(loops=1000)
def with_map_2(input_data):
    return map(MyObject.do_it, input_data)


@timy.timer(loops=1000)
def with_comprehension(input_data):
    return (
        e1.do_it()
        for e1 in input_data
    )


@timy.timer(loops=1000)
def with_map_as_list(input_data):
    return list(map(lambda foo: foo.do_it(), input_data))


@timy.timer(loops=1000)
def with_map_2_as_list(input_data):
    return list(map(MyObject.do_it, input_data))


@timy.timer(loops=1000)
def with_comprehension_as_list(input_data):
    return [
        e1.do_it()
        for e1 in input_data
    ]


if __name__ == '__main__':
    lists_size = 5000
    print(f"Lists size = {lists_size}")
    input_data = [MyObject(random.randrange(1, 100, 1)) for _ in range(lists_size)]
    print(f"For return as iterator :")
    timy_with_map = with_map(input_data)
    timy_with_map_2 = with_map_2(input_data)
    timy_with_comprehension = with_comprehension(input_data)
    print(f"For return as list :")
    timy_with_map_as_list = with_map_as_list(input_data)
    timy_with_map_as_list_2 = with_map_2_as_list(input_data)
    timy_with_comprehension_as_list = with_comprehension_as_list(input_data)
