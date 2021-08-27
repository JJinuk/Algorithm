n = list(map(int, input().split()))

double = [x ** 2 for x in n]
p = sum(double)

print(p % 10)