def word_wrap(words, width):
    # Calcula o custo de quebra de linha para cada par de palavras
    n = len(words)
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        line = -1
        for j in range(i, n):
            line += len(words[j]) + 1
            if line > width:
                cost[i][j] = float('inf')
            else:
                cost[i][j] = (width - line) ** 2

    # Calcula o custo mínimo de justificar as palavras
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    parent = [0] * n
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] + cost[j][i-1] < dp[i]:
                dp[i] = dp[j] + cost[j][i-1]
                parent[i-1] = j

    # Retorna a solução ótima
    lines = []
    i = n-1
    while i >= 0:
        j = parent[i]
        lines.append(' '.join(words[j:i+1]))
        i = j-1

    return list(reversed(lines))

# Teste
words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.']
width = 15
result = word_wrap(words, width)
for line in result:
    print(line)
