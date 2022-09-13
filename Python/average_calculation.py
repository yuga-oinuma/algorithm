# from statistics import mean

# p63


def average_calculation(datas: list) -> dict:
    sum = 0
    count = 0
    average = 0.0

    for data in datas:
        sum += data
        count += 1

    if count != 0:
        average = sum/count

    return {"sum": sum, "count": count, "average": average}


datas = [54, 20, 88, 30, 71, 29, 44, 9]
result = average_calculation(datas)
print("合計値 = %d, 有効データ数 = %d, 平均値 = %f" % (
      result["sum"], result["count"], result["average"]))


# print("合計値 = %d, 有効データ数 = %d, 平均値 = %f" % (
#       sum(datas), len(datas), mean(datas)))
