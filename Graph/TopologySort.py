from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.sort_util(i, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for ele in range(self.V):

            if visited[ele] == False:
                self.sort_util(ele, visited, stack)

        print(stack)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("The Topological Sort is:  ")
g.topological_sort()