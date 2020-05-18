import random

import timy
import numpy as np

LIST_SIZE = 10


@timy.timer(loops=10000)
def numpy_mean(data, data_2):
    return np.mean([np.mean(data), data_2])


@timy.timer(loops=10000)
def manual_mean(data, data_2):
    def manual_calc(d):
        return sum(d) / len(d)
    return manual_calc([manual_calc(data), data_2])


if __name__ == '__main__':
    lists_size = 100
    print(f"Lists size = {lists_size}")
    data = [random.randrange(1, 100, 1) for _ in range(lists_size)]
    data_2 = random.randrange(1, 100, 1)
    timy_numpy_mean = numpy_mean(data, data_2)
    timy_manual_mean = manual_mean(data, data_2)
