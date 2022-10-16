# p101

def insertion_sort(datas: list) -> list:

    for i in range(1, len(datas)+1):
        for j in reversed(range(1, i)):
            if datas[j-1] <= datas[j]:
                break
            temp = datas[j-1]
            datas[j-1] = datas[j]
            datas[j] = temp
    return datas


def disp_list(datas: list) -> None:
    for value in datas:
        print("%d" % value)


if __name__ == '__main__':
    DATAS = [35, 80, 49, 54, 11, 78, 92, 21, 67, 45]

    sorted_datas = insertion_sort(DATAS.copy())

    """
    other method
    sorted_datas = sorted(DATAS.copy())
    """

    print("ソートする前の要素値の並び")
    disp_list(DATAS)

    print("ソートした後の要素の並び")
    disp_list(sorted_datas)
