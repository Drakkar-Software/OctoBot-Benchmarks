import random

import timy
import numpy as np


@timy.timer(loops=1000)
def intersection_by_sets(list1, list2):
    return list(set(list1) & set(list2))

@timy.timer(loops=1000)
def comprehension_intersection(list1, list2):
    return [
        e1
        for e1 in list1
        if e1 in list2
    ]


if __name__ == '__main__':
    lists_size = 1000
    print(f"Lists size = {lists_size}")
    list_1 = [random.randrange(1, 100, 1) for _ in range(lists_size)]
    list_2 = [random.randrange(1, 100, 1) for _ in range(lists_size)]
    timy_intersection_by_sets = intersection_by_sets(list_1, list_2)
    timy_comprehension_intersection = comprehension_intersection(list_1, list_2)
