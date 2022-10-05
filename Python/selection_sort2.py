datas = [35, 80, 21, 54, 11, 45, 92, 39]

def selection_sort(datas: list) -> list:
    """ 単純選択ソート """
    for i in range(len(datas)-1):
        index_min = i
        for j in range(i+1, len(datas)):
            if datas[j] < datas[index_min]:
                index_min = j
        value_min = datas[index_min]
        datas[index_min] = datas[i]
        datas[i] = value_min

    return datas


def disp_list(datas: list) -> None:
    """ listの中身を1行ずつ出力する """
    for value in datas:
        print("%d" % value)


print("ソートする前の要素値の並び")
disp_list(datas)

sorted_datas = selection_sort(datas)

print("ソートした後の要素の並び")
disp_list(sorted_datas)
