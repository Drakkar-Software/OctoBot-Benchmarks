# Cython return types experiments
## Description
We wanted to test how cython return types are affecting thrown exceptions.

## Results
Exceptions are ignored for **int, double and bint** return types.
```
1
1.1
True
[1]
{1}
{'a': 1}

RuntimeError
Exception ignored in: 'cython_types.types_tests._raise_int'
Traceback (most recent call last):
  File "C:/**/OctoBot-Benchmarks/cython_types/test.py", line 5, in <module>
    types_tests.raise_int(1)
RuntimeError: 
RuntimeError
Exception ignored in: 'cython_types.types_tests._raise_double'
Traceback (most recent call last):
  File "C:/**/OctoBot-Benchmarks/cython_types/test.py", line 7, in <module>
    types_tests.raise_double(1.1)
RuntimeError: 
RuntimeError
Exception ignored in: 'cython_types.types_tests._raise_bint'
Traceback (most recent call last):
  File "C:/**/OctoBot-Benchmarks/cython_types/test.py", line 10, in <module>
    types_tests.raise_bint(True)
RuntimeError: 

Process finished with exit code 0

```