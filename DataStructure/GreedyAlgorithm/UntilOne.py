import sys

# n과 k 공백 구분하여 입력
n, k = map(int, sys.stdin.readline().split())

result = 0

# n이 k 이상이면 계속 나눈다.
while n >= k:
# n이 k로 나누어 떨어지지 X -> n에서 -1
    while n % k != 0:
        n -= 1
        result += 1

# n을 k로 나누기
        n //= k
        result += 1

while n > 1:
    n -= 1
    result += 1

print(result)
