n = int(input())

for i in range(n):
    OX = str(input())
    score = 0
    cnt = 0

    for j in list(OX):
        if j == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)