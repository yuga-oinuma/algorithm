# p97
datas = [35, 80, 21, 54, 11, 45, 92, 39]


def bubble_sort(datas: list) -> list:

    for i in reversed(range(1, len(datas))):
        for j in range(len(datas)-1):
            if datas[j] < datas[j+1]:
                temp = datas[j]
                datas[j] = datas[j+1]
                datas[j+1] = temp

    return datas


def disp_list(datas: list) -> None:
    for value in datas:
        print("%d" % value)


print("ソートする前の要素値の並び")
disp_list(datas)

sorted_datas = bubble_sort(datas)
"""
other method
sorted_datas = sorted(datas, reverse=True)
"""


print("ソートした後の要素の並び")
disp_list(sorted_datas)
