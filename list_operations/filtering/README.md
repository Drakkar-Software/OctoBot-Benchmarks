# Lists filtering
## Description
We wanted to test how to perform the better lists filtering.

## Results
With should prefer
```
def comprehension_filtering_with_iter(objects_to_filter, testing_filters):
    return [
            candidate
            for candidate in objects_to_filter
            if all(
                k in candidate
                and (v == WILDCARD or candidate[k] in [v, WILDCARD])
                for k, v in testing_filters.items()
            )
        ]
```

Timy executed (filtering_by_filter) for 1000 times in 0.016979 seconds

Timy executed (filtering_by_filter_with_iter) for 1000 times in 0.017567 seconds

Timy executed (comprehension_filtering) for 1000 times in 0.009410 seconds

Timy executed (comprehension_filtering_with_iter) for 1000 times in 0.009953 seconds


