from typing import List

def quick_sort(datas:List[int], head:int, tail:int)->List[int]:
    """
    クイックソートにて与えられた配列をソートする。

    Parameters
    ----------
    datas: List[int]
        ソート前配列
    head: int
        入れ替え位置の先頭
    tail: int
        入れ替え位置の後方
    
    Returns
    -------
    datas: List[int]
        ソート後配列
    """
    
    if head < tail:

        left = head + 1
        right = tail

        while True:

            while left < tail and datas[head] > datas[left]:
                left = left + 1
            while datas[head] < datas[right]:
                right = right - 1
            
            if left >= right:
                break

            temp = datas[left]
            datas[left] = datas[right]
            datas[right] = temp

            left = left + 1
            right = right - 1

        temp = datas[head]
        datas[head] = datas[right]
        datas[right] = temp


        quick_sort(datas, head, right - 1)
        quick_sort(datas, right + 1, tail)   

    return datas

if __name__ == '__main__':
    from random import randint

    datas = [randint(0, 100) for _ in range(12)]
    result = quick_sort(datas.copy(), 0, len(datas) - 1)

    print("ソートする前の要素値の並び :", datas)
    print("ソートする後の要素値の並び :", result)
    
