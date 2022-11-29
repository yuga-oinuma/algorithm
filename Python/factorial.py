
def factorial(n:int)->int:
    """
    与えられた整数nの階乗(n!)を求める

    Parameters
    ----------
    n: int
        対象整数

    Returns
    -------
    result: int
        nの階乗
    """
    if type(n) is not int:
        raise TypeError("引数nの型がint型ではありません")
    elif n < 0:
        raise ValueError("1以上の整数を入力してください")

    if n == 1:
        result = 1
    else:
        result = n * factorial(n -1)

    return result


if __name__ == '__main__':

    n = int(input('整数を入力してください'))
    # n='a'

    try:

        result = factorial(n)
        print('{}の階乗は{}です'.format(n, result))

    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)