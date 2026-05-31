def floyd_warshall(matrix):
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    return matrix


number_of_vertices = int(input())
graph_matrix = []

for _ in range(number_of_vertices):
    row = list(map(int, input().split()))
    graph_matrix.append(row)

shortest_paths = floyd_warshall(graph_matrix)

for row in shortest_paths:
    print(*row)