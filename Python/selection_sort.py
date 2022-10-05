datas = [35, 80, 21, 54, 11, 45, 92, 39]


def disp_array():
    for value in datas:
        print("%d" % value)


print("ソートする前の要素値の並び")
disp_array()

for i in range(len(datas)-1):
    index_min = i
    for j in range(i+1, len(datas)):
        if datas[j] < datas[index_min]:
            index_min = j
    value_min = datas[index_min]
    datas[index_min] = datas[i]
    datas[i] = value_min

print("ソートした後の要素の並び")
disp_array()


# other metohd
# print("ソートする前の要素値の並び")
# disp_array()
# datas.sort()
# print("ソートした後の要素の並び")
# disp_array()
