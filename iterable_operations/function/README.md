# Iterable function application
## Description
We wanted to test how to apply the given function to each item of a given iterable (list, tuple etc.) the most optimized way.

## Results
### For an iterable
We should prefer
```
def with_map(input_data):
    return map(func, input_data)
```

Timy executed (with_map) for 1000 times in 0.000182 seconds

Timy executed (with_comprehension) for 1000 times in 0.000273 seconds


### For a list
We should prefer for a list when len(list) > 100:
```
def with_map_as_list(input_data):
    return list(map(func, input_data))
```
With should prefer for a list when len(list) < 30:
```
def with_comprehension_as_list(input_data):
    return [
        func(e1)
        for e1 in input_data
    ]
```
Lists size = 1000

Timy executed (with_map_as_list) for 1000 times in 0.499412 seconds

Timy executed (with_comprehension_as_list) for 1000 times in 0.501223 seconds

Lists size = 20

Timy executed (with_map_as_list) for 1000 times in 0.011187 seconds

Timy executed (with_comprehension_as_list) for 1000 times in 0.009252 seconds
