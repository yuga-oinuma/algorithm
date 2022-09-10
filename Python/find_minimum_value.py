# p71
def find_minimum_value(datas: list) -> int:
    min = 9999999

    for data in datas:
        if min > data:
            min = data

    return min


datas = [540, -238, 190, 22, -645, 832, 777, -542, 0, 395]
result = find_minimum_value(datas)

print("最小値 = %d" % result)

print("最小値 = %d" % min(datas))
