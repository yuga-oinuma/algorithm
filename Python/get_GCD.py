

def get_GCD(x: int, y:int)-> int:
    """
    与えられた整数xとyの最大公約数をユークリッドの互除法により求める

    Parameters
    ----------
    x: int
        検索対象整数1
    y: int
        検索対象整数1

    Returns
    -------
    result: int
        xとyの最大公約数
    """

    if type(x) is not int or type(y) is not int:
        raise TypeError("引数xまたは引数yの型がint型ではありません")
    
    if y == 0:
        result = x
    else:
        result = get_GCD(y, x % y)
    
    return result




if __name__ == '__main__':

    x= int(input('1つ目の整数を入力してください'))
    y= int(input('2つ目の整数を入力してください'))

    # x = 'a'
    # y= 'b'

    try:

        result = get_GCD(x, y)

        print('{}と{}の最大公約数は{}です'.format(x, y, result))

    except TypeError as e:
        print(e)