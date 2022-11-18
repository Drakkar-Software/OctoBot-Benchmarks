import timy


def _update_elements(l):
    v = 1
    return [
        e + v
        for e in l
    ]


def _do_update_no_closure(input_l):
    return _update_elements(input_l)


def _do_update_closure(input_l):
    def closure_update(l):
        v = 1
        return [
            e + v
            for e in l
        ]
    return closure_update(input_l)


@timy.timer(loops=100000)
def do_update_no_closure(input_l):
    return _do_update_no_closure(input_l)


@timy.timer(loops=100000)
def do_update_closure(input_l):
    return _do_update_closure(input_l)
