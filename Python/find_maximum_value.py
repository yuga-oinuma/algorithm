# p67
def find_maximum_value(datas: list) -> int:
    max = datas[0]

    for data in datas:
        if max < data:
            max = data

    return max


datas = [540, -238, 190, 22, -645, 832, 777, -542, 0, 395]
result = find_maximum_value(datas)

print("最大値 = %d" % result)

# print("最大値 = %d" % max(datas))
