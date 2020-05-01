# List boolean checking
## Description
We wanted to test how to perform the better list boolean checking.

## Results
We should prefer
```
def loop_with_return_check():
    for v in bool_list:
        if not v:
            return False
    return True
```

*WARNING: With very large arrays (size > 10000) there is practically no difference `any` becomes very slightly better.*

Timy executed (any_check) for 10000 times in 0.032886 seconds

Timy executed (loop_with_return_check) for 10000 times in 0.024081 seconds
