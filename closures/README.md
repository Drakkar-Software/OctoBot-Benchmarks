# Closures experiments
## Description
We wanted to test if closures come at a cost compared 
to a regular function declaration.

## Results
Closures are 3% slower than regular functions in python and 16% slower in cythonized code.
### Python
```
Timy executed (do_update_no_closure) for 100000 times in 0.075869 seconds
Timy best time was 0.000001 seconds
Timy executed (do_update_closure) for 100000 times in 0.078629 seconds
Timy best time was 0.000001 seconds
```
### Cythonized
```
Timy executed (do_update_no_closure) for 100000 times in 0.027388 seconds
Timy best time was 0.000000 seconds
Timy executed (do_update_closure) for 100000 times in 0.031853 seconds
Timy best time was 0.000000 seconds
```