# Append vs Shift and set
## Description
We wanted to test if modifying the last element of a numpy array is better with `append()` or with a shift algorithm.
We should add that, in this case, we accept to loose the first element of the original array.

## Results
```
base array size = 1000
Timy executed (numpy_append) for 1000 times in 0.004942 seconds
Timy best time was 0.000004 seconds
Timy executed (numpy_shift_and_set) for 1000 times in 0.002094 seconds
Timy best time was 0.000002 seconds
```
