# Lists filtering
## Description
We wanted to test how to perform the better lists filtering.

## Results
### Without list value filtering
We should prefer
```
def comprehension_filtering(objects_to_filter, testing_filters):
    return [
            candidate
            for candidate in objects_to_filter
            if all([
                k in candidate
                and (v == WILDCARD or candidate[k] in [v, WILDCARD])
                for k, v in testing_filters.items()
            ])
        ]
```

Timy executed (filtering_by_filter) for 1000 times in 0.016979 seconds

Timy executed (filtering_by_filter_with_iter) for 1000 times in 0.017567 seconds

Timy executed (comprehension_filtering) for 1000 times in 0.008979 seconds

Timy executed (comprehension_filtering_with_iter) for 1000 times in 0.009953 seconds

### With list value filtering
We should prefer
```
def _inner_check(candidate, testing_filters):
    try:
        for k, v in testing_filters.items():
            if v == WILDCARD:
                continue
            if isinstance(candidate[k], list):
                if set(candidate[k]) & {v, WILDCARD}:
                    continue
                return False
            if candidate[k] not in [v, WILDCARD]:
                return False
        return True
    except KeyError:
        return False


@timy.timer(loops=10000)
def comprehension_filtering(objects_to_filter, testing_filters):
    return [  # from Channels._check_filters
        candidate
        for candidate in objects_to_filter
        if _inner_check(candidate, testing_filters)
    ]
```

Timy executed (filtering_by_filter) for 10000 times in 0.161933 seconds

Timy executed (comprehension_filtering) for 10000 times in 0.106281 seconds
