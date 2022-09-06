# p61
ENDDATA = -1


def items_count():
    array = [54, 20, 88, 30, 71, ENDDATA]
    count = 0
    i = 0

    while array[i] != ENDDATA:
        count += 1
        i += 1

    print("有効データ数 = %d" % count)


items_count()
