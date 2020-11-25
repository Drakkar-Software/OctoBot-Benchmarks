# cython: language_level=3,

cpdef int raise_int(int a)
cpdef double raise_double(double a)
cpdef bint raise_bint(bint a)
cpdef list raise_list(list a)
cpdef set raise_set(set a)
cpdef dict raise_dict(dict a)
cpdef object raise_object(object a)


cdef int _raise_int(int a)
cdef double _raise_double(double a)
cdef bint _raise_bint(bint a)
cdef list _raise_list(list a)
cdef set _raise_set(set a)
cdef dict _raise_dict(dict a)
cdef object _raise_object(object a)
