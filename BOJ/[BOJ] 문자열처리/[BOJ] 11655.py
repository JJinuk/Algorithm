S = input()

for i in S:
    if i.islower():
        print(chr(97 + (ord(i) + 13 - 97) % 26), end='')
    elif i.isupper():
        print(chr(65 + (ord(i) + 13 - 65) % 26), end='')
    else:
        print(i, end='')


# 1. i를 아스키 코드로 변환 후 13을 더함
# 2. 그 후, 97제외하고 26으로 나눴을 때 나머지 구함
# 3. 97부터 2에서 나온 값을 더하면 a ~ z 범위에 벗어나지 않음
# 4. 3의 값을 chr를 통해 문자로 변환