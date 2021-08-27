# 피타고라스 a^2 + b^2 == c^2 직각삼각형
import sys

while True:
    num = list(map(int, sys.stdin.readline().split()))

    if sum(num) == 0:
        break
    max_num = max(num)
    num.remove(max_num) # 빗변 길이가 세 변의 길이 중 가장 길다.
    if pow(num[0], 2) + pow(num[1], 2) == pow(max_num, 2):
        print('right')
    else:
        print('wrong')


