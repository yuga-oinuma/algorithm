# p76
def get_string_length() -> int:
    len = 0

    data = list(input('文字列を入力してください\n>'))

    for data[len] in data:
        len +=1

    return len

result = get_string_length()
print('文字長 = %d' % result )

# def other_method():
#     data = input('文字列を入力してください\n>')
#     print('文字長 = %s' % len(data) )

# other_method()