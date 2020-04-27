# Iterable member function application
## Description
We wanted to test how to apply the given member function to each item of a given iterable (list, tuple etc.) the most optimized way.

## Results
### For an iterable
We should prefer
```
def with_map(input_data):
    return map(lambda foo: foo.do_it(), input_data)
```

Timy executed (with_map) for 1000 times in 0.000209 seconds

Timy executed (with_map_2) for 1000 times in 0.000232 seconds

Timy executed (with_comprehension) for 1000 times in 0.000261 seconds

### For a list
We should prefer
```
def with_map_2_as_list(input_data):
    return list(map(MyObject.do_it, input_data))
```
Timy executed (with_map_as_list) for 1000 times in 2.867029 seconds

Timy executed (with_map_2_as_list) for 1000 times in 2.568918 seconds

Timy executed (with_comprehension_as_list) for 1000 times in 2.739427 seconds
