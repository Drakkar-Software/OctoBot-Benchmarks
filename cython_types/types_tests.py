def _raise_int(a):
    print(a)
    raise RuntimeError


def _raise_double(a):
    print(a)
    raise RuntimeError


def _raise_bint(a):
    print(a)
    raise RuntimeError


def _raise_list(a):
    print(a)
    raise RuntimeError


def _raise_set(a):
    print(a)
    raise RuntimeError


def _raise_dict(a):
    print(a)
    raise RuntimeError


def _raise_object(a):
    print(a)
    raise RuntimeError


def raise_int(a):
    return _raise_int(a)
def raise_double(a):
    return _raise_double(a)
def raise_bint(a):
    return _raise_bint(a)
def raise_list(a):
    return _raise_list(a)
def raise_set(a):
    return _raise_set(a)
def raise_dict(a):
    return _raise_dict(a)
def raise_object(a):
    return _raise_object(a)
