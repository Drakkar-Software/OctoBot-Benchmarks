import pytest
import types_tests

# does not raise when cythonized
types_tests.raise_int(1)
# does not raise when cythonized
types_tests.raise_double(1.1)
# does not raise when cythonized
# does not raise when cythonized
types_tests.raise_bint(True)
with pytest.raises(RuntimeError):
    types_tests.raise_list([1])
with pytest.raises(RuntimeError):
    types_tests.raise_set(set((1,)))
with pytest.raises(RuntimeError):
    types_tests.raise_dict({"a":1})
with pytest.raises(RuntimeError):
    types_tests.raise_object(Exception())
