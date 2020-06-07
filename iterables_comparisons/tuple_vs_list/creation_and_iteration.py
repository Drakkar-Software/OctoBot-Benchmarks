import timy


def _private_iterate_tuple(iterable_element):
    for _ in iterable_element:
        pass


@timy.timer(loops=100000)
def private_iterate_tuple(iterable_element):
    _private_iterate_tuple(iterable_element)


def _private_iterate_list(iterable_element):
    for _ in iterable_element:
        pass


@timy.timer(loops=100000)
def private_iterate_list(iterable_element):
    _private_iterate_list(iterable_element)


@timy.timer(loops=100000)
def iterate_tuple(iterable_element):
    for _ in iterable_element:
        pass


@timy.timer(loops=100000)
def iterate_list(iterable_element):
    for _ in iterable_element:
        pass


@timy.timer(loops=100000)
def create_tuple(iterable_element):
    return tuple(iterable_element)


@timy.timer(loops=100000)
def create_list(iterable_element):
    return list(iterable_element)
