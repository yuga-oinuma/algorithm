from typing import List

def insertion_sort(nums: List[int]) -> List[int]:

    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp

    return nums


if __name__ == '__main__':
    from random import randint

    # 0~99までのランダムな整数のリストを生成
    nums = [randint(0, 100) for _ in range(10)]

    sorted_nums = insertion_sort(nums.copy())

    print("ソート前のリスト")
    print(nums)

    print("ソート後のリスト")
    print(sorted_nums)
