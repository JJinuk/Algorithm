import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    next_v = permutation[v]
    if not visited[next_v]:
        dfs(next_v)

t = int(input())

for _ in range(t):
    n = int(input())
    permutation = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    cycles = 0

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cycles += 1
    print(cycles)


