# p106


from typing import List


def shell_sort(datas: List[int]) -> List:

    span = len(datas)/2
    while span > 0:
        for _ in range(int(span)):
            datas = insertion_sort(datas)
        span /= 2
    return datas


def insertion_sort(datas: List[int]) -> List[int]:

    for i in range(1, len(datas)):
        temp = datas[i]
        j = i - 1
        while j >= 0 and datas[j] > temp:
            datas[j + 1] = datas[j]
            j -= 1
        datas[j + 1] = temp

    return datas


if __name__ == '__main__':
    from random import randint

    datas = [randint(0, 100) for _ in range(12)]

    sorted_datas = shell_sort(datas.copy())

    print("'ソート前の要素の並び'")
    print(datas)

    print("'ソート後の要素の並び'")
    print(sorted_datas)
