# cython: language_level=3,

cpdef list tupled_decimal_str_constructor(tuple values)
cpdef object simple_decimal_str_constructor(double v)
cpdef list tupled_decimal_constructor(tuple values)
cpdef object simple_decimal_constructor(double v)
cpdef list tupled_float_constructor(tuple values)
cpdef double simple_float_constructor(double v)

cpdef object decimal_multiplication(object v1, object v2)
cpdef double float_multiplication(double v1, double v2)