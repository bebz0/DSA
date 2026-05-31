def dijkstra(matrix, start, finish):
    n = len(matrix)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n

    for _ in range(n):
        min_distance = float('inf')
        u = -1
        
        for i in range(n):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                u = i
                
        if u == -1:
            break
            
        visited[u] = True
        
        for v in range(n):
            if matrix[u][v] != -1 and not visited[v]:
                if distances[u] + matrix[u][v] < distances[v]:
                    distances[v] = distances[u] + matrix[u][v]

    if distances[finish] == float('inf'):
        return -1
    return distances[finish]

n, s, f = map(int, input().split())
graph_matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    graph_matrix.append(row)

result = dijkstra(graph_matrix, s - 1, f - 1)
print(result)