def calc_total(datas: list) -> int:
    total = 0

    for data in datas:
        total += data

    return total


datas = [54, 20, 88, 30, 71, 29, 44, 9, 100, 31]
total = calc_total(datas)
print("合計=%d" % total)
