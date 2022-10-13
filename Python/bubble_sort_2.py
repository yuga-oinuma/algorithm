# p97

def bubble_sort(datas: list) -> list:

    for _ in reversed(range(1, len(datas))):
        for j in range(len(datas)-1):
            if datas[j] < datas[j+1]:
                temp = datas[j]
                datas[j] = datas[j+1]
                datas[j+1] = temp

    return datas


def disp_list(datas: list) -> None:
    for value in datas:
        print("%d" % value)


if __name__ == '__main__':
    DATAS = [35, 80, 21, 54, 11, 45, 92, 39]

    sorted_datas = bubble_sort(DATAS.copy())

    print("ソートする前の要素値の並び")
    disp_list(DATAS)

    print("ソートした後の要素の並び")
    disp_list(sorted_datas)
