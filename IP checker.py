s = input().split('.')
if 0 <= int(s[0]) <= 255 and 0 <= int(s[1]) <= 255 and 0 <= int(s[2]) <= 255 and 0 <= int(s[3]) <= 255:
    print('ДА')
else:
    print('НЕТ')
