import decimal


def tupled_decimal_str_constructor(values):
    return [decimal.Decimal(str(v)) for v in values]


def simple_decimal_str_constructor(v):
    for _ in range(1000):
        decimal.Decimal(str(v))
    return decimal.Decimal(str(v))


def tupled_decimal_constructor(values):
    return [decimal.Decimal(v) for v in values]


def simple_decimal_constructor(v):
    for _ in range(1000):
        decimal.Decimal(v)
    return decimal.Decimal(v)


def tupled_float_constructor(values):
    return [float(v) for v in values]


def simple_float_constructor(v):
    for _ in range(1000):
        float(v)
    return float(v)


def decimal_multiplication(v1, v2):
    return v1 * v2


def float_multiplication(v1, v2):
    return v1 * v2
