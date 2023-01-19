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

class _DoUpdateClassMethodDefault:
    def _update_elements(self, l):
        v = 1
        return [
            e + v
            for e in l
        ]
    def do_update_no_closure(self, l):
        return self._update_elements(l)

class _DoUpdateClassMethodStatic:
    @staticmethod
    def _update_elements(self, l):
        v = 1
        return [
            e + v
            for e in l
        ]
    def do_update_no_closure(self, l):
        return self._update_elements(l)

class _DoUpdateClassMethod:
    @classmethod
    def _update_elements(cls, l):
        v = 1
        return [
            e + v
            for e in l
        ]
    def do_update_no_closure(self, l):
        return self._update_elements(l)

class _DoUpdateClassMethodClosure:
    def do_update_closure(self, l):
        def closure_update(l):
            v = 1
            return [
                e + v
                for e in l
            ]
        return closure_update(l)

class _DoUpdateClassMethodStaticClosure:
    @staticmethod
    def do_update_closure(self, l):
        def closure_update(l):
            v = 1
            return [
                e + v
                for e in l
            ]
        return closure_update(l)


@timy.timer(loops=100000)
def do_update_no_closure(input_l):
    return _do_update_no_closure(input_l)


@timy.timer(loops=100000)
def do_update_closure(input_l):
    return _do_update_closure(input_l)


@timy.timer(loops=100000)
def do_update_class_method_default(input_l):
    do_update = _DoUpdateClassMethodDefault()
    return do_update.do_update_no_closure(input_l)

@timy.timer(loops=100000)
def do_update_class_method_static(input_l):
    do_update = _DoUpdateClassMethodStatic()
    return do_update.do_update_no_closure(input_l)

@timy.timer(loops=100000)
def do_update_class_method(input_l):
    do_update = _DoUpdateClassMethod()
    return do_update.do_update_no_closure(input_l)

@timy.timer(loops=100000)
def do_update_class_method_closure(input_l):
    do_update = _DoUpdateClassMethodClosure()
    return do_update.do_update_closure(input_l)

@timy.timer(loops=100000)
def do_update_class_method_static_closure(input_l):
    do_update = _DoUpdateClassMethodStaticClosure()
    return do_update.do_update_closure(input_l)
