import heapq

# 탐색할 그래프와 시작 정점을 인수로 전달 받음
def dijkstra(graph, start, end):
    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리 생성, 무한대(inf)로 초기화
    distances = {node: [float('inf'), start] for node in graph}
    # 그래프의 시작 정점 거리는 0으로 초기화
    distances[start] = [0, start]
    # 모든 정점이 저장될 큐 생성
    queue = []
    # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소 힙에 넣어준다.
    heapq.heappush(queue, [distances[start][0], start])

    while queue:
        # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인후 업데이트
        current_distance, current_vertex = heapq.heappop(queue)
        # 더 짧은 경로가 있다면 넘어간다.
        if distances[current_vertex][0] < current_distance:
            continue
        for adj, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 혀냊 정점을 통해 가는 것이 더 가까울 경우
            if distance < distances[adj][0]:
                # 거리를 업데이트
                distances[adj] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adj])

    path = end
    path_output = end + '->'
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]
    path_output += start
    print(path_output)

    return distances


mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}}

print(dijkstra(mygraph, 'A', 'F'))
