import random

from iterables_comparisons.tuple_vs_list.creation_and_iteration import create_tuple, create_list, iterate_list, \
    iterate_tuple, private_iterate_tuple, private_iterate_list

if __name__ == '__main__':
    lists_size = 10000
    print(f"Lists size = {lists_size}")
    iterable = tuple(random.randrange(1, 100, 1) for _ in range(lists_size))
    tuple_iterable = create_tuple(iterable)
    list_iterable = create_list(iterable)
    iterate_tuple(tuple_iterable)
    iterate_list(list_iterable)
    private_iterate_tuple(tuple_iterable)
    private_iterate_list(list_iterable)
