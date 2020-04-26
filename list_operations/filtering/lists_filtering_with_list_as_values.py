import timy

WILDCARD = "*"


@timy.timer(loops=10000)
def filtering_by_filter(objects_to_filter, testing_filters):
    return list(filter(lambda x: all(
        [
            k in x
            and (v == WILDCARD
                 or x[k] in [v, WILDCARD]
                 or (isinstance(x[k], list) and set(x[k]) & {v, WILDCARD})
                 )
            for k, v in testing_filters.items()
        ]
    ), objects_to_filter))


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


if __name__ == '__main__':
    objects = [
        {"A": 1, "B": 2, "C": WILDCARD},
        {"A": False, "B": "BBBB", "C": WILDCARD},
        {"A": 3, "B": WILDCARD, "C": WILDCARD},
        {"A": WILDCARD, "B": WILDCARD, "C": WILDCARD},
        {"A": WILDCARD, "B": 2, "C": 1},
        {"A": True, "B": WILDCARD, "C": WILDCARD},
        {"A": None, "B": None, "C": WILDCARD},
        {"A": "PPP", "B": 1, "C": WILDCARD, "D": 5},
        {"A": WILDCARD, "B": 2, "C": "ABC"},
        {"A": WILDCARD, "B": True, "C": WILDCARD},
        {"A": WILDCARD, "B": 6, "C": WILDCARD, "D": WILDCARD},
        {"A": WILDCARD, "B": WILDCARD, "C": WILDCARD, "D": WILDCARD},
        {"A": None, "B": False, "C": "LLLL", "D": WILDCARD},
        {"A": None, "B": None, "C": WILDCARD, "D": None},
        {"A": WILDCARD, "B": 2, "C": WILDCARD, "D": None},
        {"A": WILDCARD, "B": [2, 3, 4, 5], "C": WILDCARD, "D": None},
        {"A": WILDCARD, "B": ["A", 5, "G"], "C": WILDCARD, "D": None},
        {"A": [1, 2, 3], "B": 2, "C": WILDCARD, "D": WILDCARD},
        {"A": ["A", "B", "C"], "B": 2, "C": WILDCARD, "D": WILDCARD},
        {"A": WILDCARD, "B": [2], "C": WILDCARD, "D": WILDCARD},
        {"A": WILDCARD, "B": ["B"], "C": WILDCARD, "D": WILDCARD}
    ]

    timy_filtering_by_filter = filtering_by_filter(objects, {"A": WILDCARD, "B": 2})
    timy_comprehension_filtering = comprehension_filtering(objects, {"A": WILDCARD, "B": 2})

    assert timy_comprehension_filtering == timy_filtering_by_filter == [
        {"A": 1, "B": 2, "C": WILDCARD},
        {"A": 3, "B": WILDCARD, "C": WILDCARD},
        {"A": WILDCARD, "B": WILDCARD, "C": WILDCARD},
        {"A": WILDCARD, "B": 2, "C": 1},
        {"A": True, "B": WILDCARD, "C": WILDCARD},
        {"A": WILDCARD, "B": 2, "C": "ABC"},
        {"A": WILDCARD, "B": WILDCARD, "C": WILDCARD, "D": WILDCARD},
        {"A": WILDCARD, "B": 2, "C": WILDCARD, "D": None},
        {"A": WILDCARD, "B": [2, 3, 4, 5], "C": WILDCARD, "D": None},
        {"A": [1, 2, 3], "B": 2, "C": WILDCARD, "D": WILDCARD},
        {"A": ["A", "B", "C"], "B": 2, "C": WILDCARD, "D": WILDCARD},
        {"A": WILDCARD, "B": [2], "C": WILDCARD, "D": WILDCARD}
    ]
