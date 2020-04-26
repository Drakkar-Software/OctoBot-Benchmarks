# Lists filtering
## Description
We wanted to test how to perform the better lists filtering.

## Results
With should prefer
```
def comprehension_filtering(objects_to_filter, testing_filters):
    return [
            candidate
            for candidate in objects_to_filter
            if all(
                [
                    k in candidate
                    and (v == WILDCARD or candidate[k] in [v, WILDCARD])
                    for k, v in testing_filters.items()
                ]
            )
        ]
```

Timy executed (filtering_by_filter) for 1000 times in 0.013476 seconds

Timy executed (comprehension_filtering) for 1000 times in 0.010402 seconds

