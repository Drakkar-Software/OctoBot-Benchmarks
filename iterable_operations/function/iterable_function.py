import math
import random

import timy


def func(n):
    return math.sqrt(n) + n ** n


@timy.timer(loops=1000)
def with_map(input_data):
    return map(func, input_data)


@timy.timer(loops=1000)
def with_comprehension(input_data):
    return (
        func(e1)
        for e1 in input_data
    )


@timy.timer(loops=1000)
def with_map_as_list(input_data):
    return list(map(func, input_data))


@timy.timer(loops=1000)
def with_comprehension_as_list(input_data):
    return [
        func(e1)
        for e1 in input_data
    ]


if __name__ == '__main__':
    lists_size = 5000
    print(f"Lists size = {lists_size}")
    input_data = [random.randrange(1, 100, 1) for _ in range(lists_size)]
    timy_with_map = with_map(input_data)
    timy_with_comprehension = with_comprehension(input_data)
    print(f"For return as list :")
    timy_with_map_as_list = with_map_as_list(input_data)
    timy_with_comprehension_as_list = with_comprehension_as_list(input_data)
