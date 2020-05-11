# Iterable function application
## Description
We wanted to test how to check the presence of an element in a dict.

## Results
We should prefer using the ```in``` operator in a ```set``` of the ```dict keys```

```python
element in set(elements.keys())
```


Timy executed (with_map) for 1000 times in 0.000182 seconds

Timy executed (with_comprehension) for 1000 times in 0.000273 seconds

Lists size = 50

Timy executed (with_in) for 1000000 times in 0.335204 seconds
Timy best time was 0.000000 seconds
Timy executed (with_select_val) for 1000000 times in 0.488389 seconds
Timy best time was 0.000000 seconds
Timy executed (with_in) for 1000000 times in 0.323887 seconds
Timy best time was 0.000000 seconds
Timy executed (with_in) for 1000000 times in 0.324952 seconds
Timy best time was 0.000000 seconds
Timy executed (with_in) for 1000000 times in 11.920266 seconds
Timy best time was 0.000011 seconds
