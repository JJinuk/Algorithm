n = int(input())
res = ''

if n == 0:
    print(0)
else:
    while n:
        res += str(n % 2)
        n //= 2
        n *= -1
    print(res[::-1])