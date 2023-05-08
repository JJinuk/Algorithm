a, b = map(int, input().split())
m = int(input())
num = list(map(int, input().split()))[::-1]

decimal = 0
for i in range(m):
    decimal += num[i] * (a ** i)

converted_num = []
while decimal:
    converted_num.append(decimal % b)
    decimal //= b
print(*converted_num[::-1])