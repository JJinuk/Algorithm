# dynamic programming
# memoization(Top - Down)

dp = [0] * 100  # 결과를 저장할 리스트
dp[0] = 1
dp[1] = 1


def fib(n):
    # 만약 계산한 적이 없다면 재귀로 계산.
    if dp[n] == 0:
        dp[n] = fib(n - 1) + fib(n - 2)

        # 계산한 적이 있다면 그대로 반환
        return dp[n]


fib(10)
