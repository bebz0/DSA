def bellman_ford(number_of_vertices, edges, start_vertex):
    distances = [30000] * (number_of_vertices + 1)
    distances[start_vertex] = 0

    for _ in range(number_of_vertices - 1):
        for start_node, end_node, weight in edges:
            if distances[start_node] != 30000 and distances[start_node] + weight < distances[end_node]:
                distances[end_node] = distances[start_node] + weight

    return distances[1:]

number_of_vertices, number_of_edges = map(int, input().split())
graph_edges = []

for _ in range(number_of_edges):
    start_node, end_node, edge_weight = map(int, input().split())
    graph_edges.append((start_node, end_node, edge_weight))

shortest_distances = bellman_ford(number_of_vertices, graph_edges, 1)

print(*shortest_distances)