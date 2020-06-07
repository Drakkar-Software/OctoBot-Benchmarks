# Tuples vs lists
## Description
We wanted to figure out when to use tuples and when to use lists.

## Results
When creating an immutable iterable, we should prefer ```tuple```  
When iterating over an immutable iterable, we should prefer ```list```

> In both cases (list and tuples), iterating is ~5 times faster when cythonized.  
> Wrapping an iterator into a private cython function slow down the execution.

### Python
```
Lists size = 10000
Timy executed (create_tuple) for 100000 times in 0.033617 seconds
Timy best time was 0.000000 seconds
Timy executed (create_list) for 100000 times in 2.065165 seconds
Timy best time was 0.000015 seconds
Timy executed (iterate_tuple) for 100000 times in 6.806723 seconds
Timy best time was 0.000064 seconds
Timy executed (iterate_list) for 100000 times in 6.120964 seconds
Timy best time was 0.000058 seconds
Timy executed (private_iterate_tuple) for 100000 times in 6.653825 seconds
Timy best time was 0.000064 seconds
Timy executed (private_iterate_list) for 100000 times in 6.137208 seconds
Timy best time was 0.000058 seconds
```

### Compiled
```
Lists size = 10000
Timy executed (create_tuple) for 100000 times in 0.010181 seconds
Timy best time was 0.000000 seconds
Timy executed (create_list) for 100000 times in 1.576709 seconds
Timy best time was 0.000012 seconds
Timy executed (iterate_tuple) for 100000 times in 1.370309 seconds
Timy best time was 0.000013 seconds
Timy executed (iterate_list) for 100000 times in 1.242398 seconds
Timy best time was 0.000012 seconds
Timy executed (private_iterate_tuple) for 100000 times in 1.539408 seconds
Timy best time was 0.000013 seconds
Timy executed (private_iterate_list) for 100000 times in 1.355430 seconds
Timy best time was 0.000013 seconds
```
