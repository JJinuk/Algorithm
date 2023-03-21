import sys

A = [0]

n = int(sys.stdin.readline())
for _ in range(n):
    A.append(int(sys.stdin.readline()))

if n == 1:
    print(A[1])
else:
    dp = [0]*(n+1)
    dp[1] = A[1]
    dp[2] = A[1]+A[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+A[i-1]+A[i], dp[i-2]+A[i])
    
    print(dp[-1])