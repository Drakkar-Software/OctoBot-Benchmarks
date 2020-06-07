# cython: language_level=3,

cpdef void iterate_tuple(tuple iterable_element)
cpdef void iterate_list(list iterable_element)
cpdef tuple create_tuple(tuple iterable_element)
cpdef list create_list(tuple iterable_element)

cpdef void private_iterate_tuple(tuple iterable_element)
cdef void _private_iterate_tuple(tuple iterable_element)

cpdef void private_iterate_list(tuple iterable_element)
cdef void _private_iterate_list(list iterable_element)
