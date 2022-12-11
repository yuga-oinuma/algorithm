import math


def newtons_method(value: float)->float:
    """
    与えられた整数の平方根をニュートン法により求める

    Parameters
    ----------
    value: float
        対象整数

    Returns
    -------
    result: float
        valueの平方根
    """
    if type(value) is not float:
        raise TypeError('入力された整数がfloat型ではありません')
    elif value < 0:
        raise ValueError('1以上の整数を入力してください')


    MAXLOOP = 100
    EV = 0.0000001
    x0 = value
    x1= 0

    delta = EV

    for i in range(MAXLOOP):
        if math.fabs(delta) < EV:
            break

        delta = (x0 * x0 - value)/(2.0 * x0)
        x1 = x0 - delta
        x0 = x1

    return x1

if __name__ == '__main__':

    try:
        value = float(input('平方根を求める数値を入力してください'))
        # value = 'a'

        result = newtons_method(value)
        
        print('{}の平方根（近似値）は{:.08f}です。'.format(value, result))
        
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

