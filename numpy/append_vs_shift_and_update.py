import timy
import numpy as np


@timy.timer(loops=1000)
def numpy_append(numpy_base_array, kline_data):
    return np.append(numpy_base_array, kline_data)


def shift(arr, num, fill_value=np.nan):
    result = np.empty_like(arr)
    if num > 0:
        result[:num] = fill_value
        result[num:] = arr[:-num]
    elif num < 0:
        result[num:] = fill_value
        result[:num] = arr[-num:]
    else:
        result[:] = arr
    return result


@timy.timer(loops=1000)
def numpy_shift_and_set(numpy_base_array, kline_data):
    return shift(numpy_base_array, -1, fill_value=kline_data)


if __name__ == '__main__':
    base_array_size = 1000
    print(f"base array size = {base_array_size}")
    numpy_base_array = np.random.uniform(low=0, high=10000, size=base_array_size)
    kline_data = np.random.randint(low=0, high=1000)
    timy_numpy_append = numpy_append(numpy_base_array, kline_data)
    timy_numpy_shift_and_set = numpy_shift_and_set(numpy_base_array, kline_data)
