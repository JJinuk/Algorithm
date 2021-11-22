from collections import defaultdict


# 방향 그래프를 인접 리스트로 표현

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)          # 그래프를 저장할 dic

    def addEdge(self, u, v):                    # 그래프에 edge를 추가하는 함수
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):              # DFS에 사용될 함수
        visited.add(v)                          # 방문한 현재 노드에 표시해주고 출력한다.
        print(v, end=' ')

        for i in self.graph[v]:                 # 모든 정점에 대해 반복
            if i not in visited:                # 인접한 정점
                self.DFSUtil(i, visited)

        def DFS(self, v):                       # DFS 함수
            visited = set()                     # 방문한 정점을 저장할 set() 생성
        self.DFSUtil(v, visited)                # DFS출력을 도와줄 재귀함수 호출


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Vertex 2부터 시작")
g.DFS(2)
