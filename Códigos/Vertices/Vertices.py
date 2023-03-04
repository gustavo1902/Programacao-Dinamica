class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

def vertex_cover(graph):
    n = graph.n
    dp = [[0, 0] for _ in range(n)]

    def dfs(u, p):
        for v in graph.adj[u]:
            if v != p:
                dfs(v, u)
                dp[u][0] += min(dp[v][0], dp[v][1])
                dp[u][1] += dp[v][0]

        dp[u][1] += 1

    dfs(0, -1)
    return min(dp[0][0], dp[0][1])

# Teste
g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
result = vertex_cover(g)
print(result) # Deve imprimir 3
