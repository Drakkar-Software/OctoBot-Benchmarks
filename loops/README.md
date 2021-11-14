# Looping optimization
## Description
We wanted to figure out the faster way to iterate over a non-static range of elements.

## Results
We should prefer traditional for loops with nested if statements.
```
def with_traditional_loop(iterable):
    result = 0
    for element in iterable:
        if condition(element):
            result = iterate(result, element)
    return result
```

```
very small list
Timy executed (with_comprehension_list) for 1000 times in 0.000719 seconds
Timy best time was 0.000001 seconds
Timy executed (with_comprehension_tuple) for 1000 times in 0.000923 seconds
Timy best time was 0.000001 seconds
Timy executed (with_generator) for 1000 times in 0.000732 seconds
Timy best time was 0.000001 seconds
Timy executed (with_traditional_loop) for 1000 times in 0.000509 seconds
Timy best time was 0.000000 seconds
small list
Timy executed (with_comprehension_list) for 1000 times in 0.001404 seconds
Timy best time was 0.000001 seconds
Timy executed (with_comprehension_tuple) for 1000 times in 0.001657 seconds
Timy best time was 0.000002 seconds
Timy executed (with_generator) for 1000 times in 0.001554 seconds
Timy best time was 0.000001 seconds
Timy executed (with_traditional_loop) for 1000 times in 0.001173 seconds
Timy best time was 0.000001 seconds
medium list
Timy executed (with_comprehension_list) for 1000 times in 0.005991 seconds
Timy best time was 0.000006 seconds
Timy executed (with_comprehension_tuple) for 1000 times in 0.006613 seconds
Timy best time was 0.000006 seconds
Timy executed (with_generator) for 1000 times in 0.006455 seconds
Timy best time was 0.000006 seconds
Timy executed (with_traditional_loop) for 1000 times in 0.005238 seconds
Timy best time was 0.000005 seconds
large list
Timy executed (with_comprehension_list) for 1000 times in 0.057426 seconds
Timy best time was 0.000055 seconds
Timy executed (with_comprehension_tuple) for 1000 times in 0.061664 seconds
Timy best time was 0.000060 seconds
Timy executed (with_generator) for 1000 times in 0.062775 seconds
Timy best time was 0.000057 seconds
Timy executed (with_traditional_loop) for 1000 times in 0.053019 seconds
Timy best time was 0.000051 seconds
very large list
Timy executed (with_comprehension_list) for 1000 times in 0.567988 seconds
Timy best time was 0.000524 seconds
Timy executed (with_comprehension_tuple) for 1000 times in 0.617621 seconds
Timy best time was 0.000571 seconds
Timy executed (with_generator) for 1000 times in 0.623674 seconds
Timy best time was 0.000563 seconds
Timy executed (with_traditional_loop) for 1000 times in 0.531900 seconds
Timy best time was 0.000499 seconds

Process finished with exit code 0

```

### Cython