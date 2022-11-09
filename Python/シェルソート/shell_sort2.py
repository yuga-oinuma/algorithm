from typing import List


def shell_sort(datas: List[int]) -> List:
    def insertion_sort(datas: List[int]) -> List[int]:
        for i in range(1, len(datas)):
            temp = datas[i]
            j = i - 1
            while j >= 0 and datas[j] > temp:
                datas[j + 1] = datas[j]
                j -= 1
            datas[j + 1] = temp

        return datas


    span = len(datas)/2
    while span > 0:
        for _ in range(int(span)):
            datas = insertion_sort(datas)
        span /= 2
    return datas


if __name__ == '__main__':
    from time import time
    from random import randint

    time_start = time()
    datas = [randint(0, 100) for _ in range(12)]

    sorted_datas = shell_sort(datas.copy())

    time_stop = time()
    time_total = time_stop - time_start
    print("Time:  ", time_total)
    print("Before:", datas)
    print("After: ", sorted_datas)
