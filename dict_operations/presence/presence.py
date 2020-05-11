import uuid
import timy


@timy.timer(loops=1000000)
def with_in(val1, val2, elements):
    return val1 in elements and val2 in elements


@timy.timer(loops=1000000)
def with_select_val(val1, val2, elements):
    try:
        return elements[val1], elements[val2]
    except KeyError:
        return False


if __name__ == '__main__':
    elements = {uuid.uuid4(): uuid.uuid4()
                for _ in range(50)}
    for i, key in enumerate(elements.keys()):
        if i == 25:
            break
    with_in_val = with_in(key, "1", elements)
    with_select = with_select_val(key, "1", elements)
    with_set_from_keys = with_in(key, "1", set(elements.keys()))
    with_set_from_list = with_in(key, "1", set(list(elements)))
    with_list = with_in(key, "1", list(elements))
