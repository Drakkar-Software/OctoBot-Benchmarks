import random

import timy


@timy.timer(loops=10000)
def filter_by_native_filter(list1):
    return list(filter(lambda x: x < 500, list1))


@timy.timer(loops=10000)
def comprehension_filtering(list1):
    return [
        x
        for x in list1
        if x < 500
    ]


if __name__ == '__main__':
    lists_size = 1000
    print(f"Lists size = {lists_size}")
    list_1 = [random.randrange(1, 1000, 1) for _ in range(lists_size)]
    timy_filter_by_native_filter = filter_by_native_filter(list_1)
    timy_comprehension_filtering = comprehension_filtering(list_1)
