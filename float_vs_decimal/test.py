import timy
from float_vs_decimal.comparator import *


@timy.timer(loops=1000)
def timed(func, *args):
    return func(*args)


if __name__ == '__main__':
    lists_size = 999
    print(f"Values count = {lists_size}")
    values = tuple(10/i for i in range(1, lists_size+1))

    print("tupled_float_constructor")
    float_values = timed(tupled_float_constructor, values)
    print("tupled_decimal_constructor")
    decimal_values = timed(tupled_decimal_constructor, values)
    print("tupled_decimal_str_constructor")
    decimal_values = timed(tupled_decimal_str_constructor, values)

    value = 1.2
    print("simple_float_constructor")
    float_value = timed(simple_float_constructor, value)
    print("simple_decimal_constructor")
    decimal_value = timed(simple_decimal_constructor, value)
    print("simple_decimal_str_constructor")
    decimal_value = timed(simple_decimal_str_constructor, value)

    v1 = 1.2
    v2 = 3515.124771
    print("decimal_multiplication")
    decimal_value = timed(decimal_multiplication, decimal.Decimal(str(v1)), decimal.Decimal(str(v2)))
    print("float_multiplication")
    decimal_value = timed(float_multiplication, v1, v2)
