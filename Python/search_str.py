
from time import time


def search_str(sentence: str, target: str) ->int:
    result = -1
    i = j = 0
    
    while i < len(sentence) and j < len(target):
        if sentence[i] == target[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0

    result = i - j

    return result



if __name__ == '__main__':
    
    
    sentence = input('探索される文字列を入力してください\n>')
    target = input('探索する部分文字列を入力してください\n>')

    try:
        time_start = time()
        result = search_str(sentence, target)
        time_stop = time()
        time_total = time_stop - time_start
        print("Time:  ", time_total)
        if result == -1:
            print('部分文字列は見つかりませんでした')
        else:
            print('部分文字列の添字は %d です' % result)
    except:
        print('問題が発生しました。やり直してください')

    