import sys

n, m, k = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

data.sort()

first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수
count = int(m / (k + 1)) * k + (m % (k + 1))

result = 0
result += count * first
result += (m - count) * second

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#
#     if m == 0:
#         break
#     result += second
#     m -= 1

print(result)

