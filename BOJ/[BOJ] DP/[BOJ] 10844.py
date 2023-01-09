n = int(input())

dp = [[0] * 10 for _ in range(n+1)]     # n개의 테이블
for i in range(1, 10):                  # 초기화, n이 1인 경우(0번째)에 값을 처음에 입력해주겠다는 의미
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % pow(10, 9))