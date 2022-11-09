from typing import List

def binary_search(datas: List[int], target: int)-> int:
    result =  -1
    head = 0
    tail = len(datas) - 1
    while result == -1 and head <= tail:
        middle = int((head + tail)/2)
        if datas[middle] == target:
            result = middle
        elif datas[middle] < target:
            head = middle +1
        else: 
            tail = middle - 1
    
    return result



if __name__ == '__main__':
    datas = [2, 10, 21, 28, 33, 54, 60, 63, 71, 79, 82, 87, 88, 94, 97]

    target = input('探索する値を入力してください\n>')
    result = binary_search(datas, int(target))
    if result == -1:
        print("目的の値は見つかりませんでした")
    else:
        print("目的の値の添え字は %d です。" % result)