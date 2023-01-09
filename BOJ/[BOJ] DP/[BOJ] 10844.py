n = int(input())

dp = [[0] * 10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1

for j in range(2, n+1):
    for k in range(10):
        if k == 0:
            dp[j][k] = dp[j-1][1]
        elif k == 9:
            dp[j][k] = dp[j-1][8]
        else:
            dp[j][k] = dp[j-1][k-1] + dp[j-1][k+1]

print(sum(dp[n]) % pow(10, 9))