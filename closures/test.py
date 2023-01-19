import closures_tests
import timy


def get_list(max):
    return [
        i
        for i in range(max)
    ]


closures_tests.do_update_no_closure(get_list(10))
closures_tests.do_update_closure(get_list(10))
closures_tests.do_update_class_method_default(get_list(10))
closures_tests.do_update_class_method(get_list(10))
closures_tests.do_update_class_method_static(get_list(10))
closures_tests.do_update_class_method_closure(get_list(10))
closures_tests.do_update_class_method_static_closure(get_list(10))
