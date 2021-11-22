from collections import defaultdict


# 그래프 클래스는 방향이 있는 그래프
# 인접 리스트 사용


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # 그래프를 저장할 기본 dic

    def addEdge(self, u, v):  # 그래프에 Edge를 추가할 함수
        self.graph[u].append(v)

    def BFS(self, s):   # BFS 그래프를 출력할 함수
        visited = [False] * (max(self.graph) + 1)   # 모즌 정점을 방문X로 표시

        queue = []  # BFS를 위한 큐 생성

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)            # 정점에서 dequeue
            print(s, end=" ")           # 큐 출력

            for i in self.graph[s]:     # 인접한 모든 정점 가져오기, 인접한 경우 정점 s 제거
                if not visited[i]:      # 방문하지 않았으면
                    queue.append(i)     # 방문 -> enqueue
                    visited[i] = True


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Vertex 2부터 시작")

g.BFS(2)
