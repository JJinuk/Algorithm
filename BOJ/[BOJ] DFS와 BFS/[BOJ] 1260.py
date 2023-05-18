from collections import deque

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited_dfs[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_dfs = [False] * (n+1)
dfs(v)
print()

visited_bfs = [False] * (n+1)
bfs(v)