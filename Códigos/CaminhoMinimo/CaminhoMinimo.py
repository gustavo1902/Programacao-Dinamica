INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    dist = [[graph[i][j] if graph[i][j] != 0 else INF for j in range(n)] for i in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

graph = [[0, 2, 5, 0, 0],
         [2, 0, 1, 0, 4],
         [5, 1, 0, 3, 0],
         [0, 0, 3, 0, 2],
         [0, 4, 0, 2, 0]]

distances = floyd_warshall(graph)
print(distances)
