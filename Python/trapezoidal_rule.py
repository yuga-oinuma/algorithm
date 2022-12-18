
def f(x: float)-> float:
    return x**2 + 5.0 * x + 6.0


def trapezoidal_rule (value_a:float, value_b:float)->float:

    """
    台形法により、関数f(x)= x^2+5x+6を区間[a, b]で定積分した近似値を求める


    Parameters
    ----------
    value_a: float
        区間a
    valie_b: float
        区間b

    Returns
    -------
    result: float
        入力された区間で定積分した近似値
    """

    if type(value_a) is not float or type(value_b) is not float:
        raise TypeError('入力された整数がfloat型ではありません')

    N = 10000

    dx = (value_b - value_a) / N
    s = (f(value_a) + f(value_b)) / 2.0

    for i in range(1, N - 1):
        s = s + f(value_a + dx * i)
    s = s * dx

    return s


if __name__ == '__main__':

    try:
        value_a , value_b = (float(x) for x in input('区間[a, b]を入力してください:').split())
        # value_a = 'a'
        # value_b = 'b'

        result = trapezoidal_rule(value_a, value_b)
        
        print('近似値は{:.08f}です。'.format(result))
        
    except TypeError as e:
        print(e)
