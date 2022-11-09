from typing import List


def linear_search(datas: List[int], target: int) -> int:
    result = -1

    for i in range(len(datas)):
        if datas[i] == target:
            result = i
    return result


if __name__ == '__main__':
    datas = [35, 80, 21, 54, 11, 92, 23, 2, 67, 45]
    target = input('探索する値を入力してください\n>')
    result = linear_search(datas, int(target))
    if result == -1:
        print("目的の値は見つかりませんでした")
    else:
        print("目的の値の添え字は %d です。" % result)
