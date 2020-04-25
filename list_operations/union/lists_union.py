import random

import timy
import numpy as np


@timy.timer(loops=1000)
def union_by_sets(list1, list2):
    return list(set().union(list1, list2))  # can be used for more than 2 lists : set().union(list1, list2, list3...)


@timy.timer(loops=1000)
def append_based_union(list1, list2):
    return set(list1 + list2)


if __name__ == '__main__':
    lists_size = 1000
    print(f"Lists size = {lists_size}")
    list_1 = [random.randrange(1, 100, 1) for _ in range(lists_size)]
    list_2 = [random.randrange(1, 100, 1) for _ in range(lists_size)]
    timy_union_by_sets = union_by_sets(list_1, list_2)
    timy_append_based_union = append_based_union(list_1, list_2)
