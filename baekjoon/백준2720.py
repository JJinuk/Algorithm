# 테스트 케이스 입력
# 테스트 케이스 갯수만큼 센트 입력
# 124센트는 4($0.25)쿼터 2($0.10)다임, 0($0.05)니켈, 4($0.01)페니

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    C = int(sys.stdin.readline())
    coin = [25, 10, 5, 1]
    L = []

    for i in coin:
        L.append(C // i)
        C = C % i

    print(*L)


    # Q = C // 25
    # D = (C % 25) // 10
    # N = (C % 25) % 10 // 5
    # P = (C % 25) % 10 % 5 // 1

    # print(Q, D, N, P)

