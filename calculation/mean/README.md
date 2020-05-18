# Average calculation
## Description
We wanted to test how to perform the average calculation between a list of float and a float.

## Results
We should prefer
```
def manual_mean(data, data_2):
    def manual_calc(d):
        return sum(d) / len(d)
    return manual_calc([manual_calc(data), data_2])
```

Lists size = 100
Timy executed (numpy_mean) for 10000 times in 0.204180 seconds

Timy executed (manual_mean) for 10000 times in 0.007851 seconds
