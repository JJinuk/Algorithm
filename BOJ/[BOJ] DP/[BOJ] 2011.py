import sys

n = list(map(int, sys.stdin.readline().strip()))

if n[0] == 0:
    print(0)
else:
    n = [0] + n
    dp = [0] * len(n)
    dp[0] = dp[1] = 1

    for i in range(2, len(n)):
        if n[i] > 0:
            dp[i] += dp[i-1]
        
        tmp = n[i-1] * 10 + n[i]

        if 9 < tmp < 27:
            dp[i] += dp[i-2]

        dp[i] %= 1000000
    print(dp[-1] % 1000000)