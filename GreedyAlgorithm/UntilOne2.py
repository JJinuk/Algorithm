import sys

n, k = map(int, sys.stdin.readline().split())

result = 0

while True:
# n == k로 누어 떨어지는 수가 될 때까지 1씩 뻰다.
    target = (n // k) * k
    result += (n - target)
    n = target
# n이 k보다 작을 경우(나눌 수 없는)반복문 탈출
    if n < k:
        break
# k로 나눈다.
    result += 1
    n //= k

# 마지막 남은 수에 1씩 뻬줌
result += (n - 1)
print(result)