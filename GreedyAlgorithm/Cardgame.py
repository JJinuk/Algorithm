import sys
# n과 m 공백 구분 입력(열x행)
n, m = map(int, sys.stdin.readline().split())

result = 0
# 한 줄씩 입력
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
# 현재 줄에서 최소
    min_value = min(data)
# 가장 작은 수들 중 최대
    result = max(result, min_value)

# for i in range(n):
#     data = list(map(int, sys.stdin.readline().split()))
#     min_value = 10001
#     for a in data:
#         min_value = min(min_value, a)
# # 가장 작은 수들 중 큰 수 찾기
#     result = max(result, min_value)

print(result)