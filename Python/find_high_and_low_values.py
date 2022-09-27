# p79

MAX = 9999
MIN = -9999
datas = [20, 29, 30, 44, 51, 66, 72, 78, 80, 87]


def find_high_and_low_values():

    data = input('数値M (1~100)を指定してください\n')

    high = higher(int(data))
    low = lower(int(data))

    print('%s より大きい値は' % data)
    if high == MAX:
        print('ありませんでした。')
    else:
        print('%d です' % high)

    print('%s より小さい値は' % data)
    if low == MIN:
        print('ありませんでした。')
    else:
        print('%d です' % low)


def higher(data) -> int:
    datas.append(MAX)
    i = 0
    while datas[i] <= data:
        i = i+1

    return datas[i]


def lower(data) -> int:
    datas[len(datas) - 1] = MIN
    i = 0
    while datas[i] >= data:
        i = i+1

    return datas[i]


find_high_and_low_values()


# def other_method():
#     data = input('数値M (1~100)を指定してください\n')

#     high = list(filter(lambda x: x >= int(data), datas))
#     low = list(filter(lambda x: x <= int(data), datas))

#     print('%s より大きい値は' % data)
#     if bool(high) == False:
#         print('ありませんでした。')
#     else:
#         print('%d です' % high[0])

#     print('%s より小さい値は' % data)
#     if bool(low) == False:
#         print('ありませんでした。')
#     else:
#         print('%d です' % low[0])


# other_method()
