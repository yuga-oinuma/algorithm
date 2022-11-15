def search_str(sentence: str, target: str) -> int:
    """
    検索対象文字列の中に検索文字（1文字）が含まれている場合、最初に出現するインデックスを返す
    含まれていない場合は -1 を返す

    Parameters
    ----------
    sentence: str
        検索対象文字列
    target: str
        検索文字（1文字）

    Returns
    -------
    idx: int
        検索される文字列のインデックス
    """
    if type(sentence) is not str or type(target) is not str:
        raise TypeError("引数sentenceまたは引数targetの型がstrではありません")
    elif len(target) > 1:
        raise ValueError("引数targetの長さが1より大きいです")

    idx = -1

    for i in range(len(sentence)):
        if sentence[i] == target:
            idx = i

    return idx


if __name__ == '__main__':
    sentence = "hoge"
    target = 5
    # sentence = input('探索される文字列を入力してください\n>')
    # target = input('探索する部分文字列を入力してください\n>')

    try:
        result = search_str(sentence, target)
        if result == -1:
            print('{} は {} の中に含まれていません'.format(target, sentence))
        else:
            print('{} は {} の {} 番目に含まれています'.format(target, sentence, result + 1))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

