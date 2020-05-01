import random

import timy

LIST_SIZE = 10


@timy.timer(loops=10000)
def loop_with_return_check():
    bool_list = [bool(random.getrandbits(1)) for _ in range(LIST_SIZE)]
    for v in bool_list:
        if not v:
            return False
    return True


@timy.timer(loops=10000)
def any_check():
    bool_list = [bool(random.getrandbits(1)) for _ in range(LIST_SIZE)]
    return any(v for v in bool_list)


if __name__ == '__main__':
    timy_any_check = any_check()
    timy_loop_with_return_check = loop_with_return_check()
