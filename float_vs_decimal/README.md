# Cython return types experiments
## Description
We wanted to test the performance costs of using decimal.Decimal instead of native float representation.

## Results

### Cythonized
```
tupled_float_constructor
Timy executed (timed) for 1000 times in 0.008012 seconds
Timy best time was 0.000007 seconds
tupled_decimal_constructor
Timy executed (timed) for 1000 times in 1.362506 seconds
Timy best time was 0.000840 seconds
tupled_decimal_str_constructor
Timy executed (timed) for 1000 times in 1.512435 seconds
Timy best time was 0.001328 seconds
simple_float_constructor
Timy executed (timed) for 1000 times in 0.000218 seconds
Timy best time was 0.000000 seconds
simple_decimal_constructor
Timy executed (timed) for 1000 times in 0.843575 seconds
Timy best time was 0.000780 seconds
simple_decimal_str_constructor
Timy executed (timed) for 1000 times in 0.427359 seconds
Timy best time was 0.000404 seconds
decimal_multiplication
Timy executed (timed) for 1000 times in 0.000221 seconds
Timy best time was 0.000000 seconds
float_multiplication
Timy executed (timed) for 1000 times in 0.000176 seconds
Timy best time was 0.000000 seconds
```

### Python
```
tupled_float_constructor
Timy executed (timed) for 1000 times in 0.068723 seconds
Timy best time was 0.000062 seconds
tupled_decimal_constructor
Timy executed (timed) for 1000 times in 0.922099 seconds
Timy best time was 0.000861 seconds
tupled_decimal_str_constructor
Timy executed (timed) for 1000 times in 1.485819 seconds
Timy best time was 0.001383 seconds
simple_float_constructor
Timy executed (timed) for 1000 times in 0.066386 seconds
Timy best time was 0.000063 seconds
simple_decimal_constructor
Timy executed (timed) for 1000 times in 0.887436 seconds
Timy best time was 0.000809 seconds
simple_decimal_str_constructor
Timy executed (timed) for 1000 times in 0.494698 seconds
Timy best time was 0.000452 seconds
decimal_multiplication
Timy executed (timed) for 1000 times in 0.000284 seconds
Timy best time was 0.000000 seconds
float_multiplication
Timy executed (timed) for 1000 times in 0.000249 seconds
Timy best time was 0.000000 seconds
```

## Conclusion
### Constructors
decimal.Decimal are much slower to create than floats (~8x).
Cythonization makes float creation much faster (~12x) while it makes decimal.Decimal 
operations just a little faster (~10%).

### Operations
decimal.Decimal operations are comparable to floats in time on python but ~33% slower when cythonized  

### decimal.Decimal(str()) vs decimal.Decimal()
Decimal creation using decimal.Decimal(str(float_value)) is ~2x faster than creating it 
using decimal.Decimal(float_value)
```
