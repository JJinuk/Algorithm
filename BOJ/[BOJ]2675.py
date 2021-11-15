n = int(input())

for _ in range(n):
    cnt, w = input().split()
    for x in w:
        print(x*int(cnt), end='')
    print()