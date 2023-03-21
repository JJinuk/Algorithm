import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [x for x in A]         # n번째 수까지 포함된 연속된 수의 합 중 최대값

for i in range(1, n):
    dp[i] = max(dp[i], dp[i]+dp[i+1])
    

print(max(dp))