import timy


def iterate(i, addition):
    return i + addition


def condition(element):
    return element % 2 == 0


@timy.timer(loops=1000)
def with_comprehension_list(iterable):
    result = 0
    for element in [element for element in iterable if condition(element)]:
        result = iterate(result, element)
    return result


@timy.timer(loops=1000)
def with_comprehension_tuple(iterable):
    result = 0
    for element in tuple(element for element in iterable if condition(element)):
        result = iterate(result, element)
    return result


@timy.timer(loops=1000)
def with_generator(iterable):
    result = 0
    for element in (element for element in iterable if condition(element)):
        result = iterate(result, element)
    return result


@timy.timer(loops=1000)
def with_traditional_loop(iterable):
    result = 0
    for element in iterable:
        if condition(element):
            result = iterate(result, element)
    return result


def comp(iterable_size):
    iterable = [i for i in range(iterable_size)]
    r1 = with_comprehension_list(iterable)
    r2 = with_comprehension_tuple(iterable)
    r3 = with_generator(iterable)
    r4 = with_traditional_loop(iterable)
    assert r1 == r2 == r3 == r4
    return r1
