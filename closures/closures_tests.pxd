# cython: language_level=3,

cdef list _update_elements(list l)
cdef list _do_update_no_closure(list l)
cdef list _do_update_closure(list l)

# cdef list do_update_class_method_default(list l)
# cdef list do_update_class_method_static(list l)
# cdef list do_update_class_method(list l)
# cdef list do_update_class_method_closure(list l)
# cdef list do_update_class_method_static_closure(list l)

cdef class _DoUpdateClassMethodDefault:
    cdef list _update_elements(self, list l)
    cdef list do_update_no_closure(self, list l)
#     
cdef class _DoUpdateClassMethodStatic:
    cdef list _update_elements(self, list l)
    cdef list do_update_no_closure(self, list l)

cdef class _DoUpdateClassMethod:
    cdef list _update_elements(cls, list l)
    cdef list do_update_no_closure(self, list l)

cdef class _DoUpdateClassMethodClosure:
    cdef list do_update_closure(self, list l)

cdef class _DoUpdateClassMethodStaticClosure:
    cdef list do_update_closure(self, list l)
