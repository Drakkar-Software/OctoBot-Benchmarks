# Lists simple filtering
## Description
We wanted to test how to perform the better lists simple filtering.

## Results
We should prefer
```
def comprehension_filtering(list1):
    return [
        x
        for x in list1
        if x < 500
    ]
```

Lists size = 100
Timy executed (filter_by_native_filter) for 10000 times in 0.086905 seconds
Timy executed (comprehension_filtering) for 10000 times in 0.034475 seconds

Lists size = 1000
Timy executed (filter_by_native_filter) for 10000 times in 0.730850 seconds
Timy executed (comprehension_filtering) for 10000 times in 0.340609 seconds
