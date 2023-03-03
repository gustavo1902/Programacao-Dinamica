def mochila(capacidade, pesos, valores, n):
    # Inicializa a tabela com valores zero
    tabela = [[0 for x in range(capacidade + 1)] for x in range(n + 1)]
 
    # Preenche a tabela iterativamente
    for i in range(n + 1):
        for w in range(capacidade + 1):
            if i == 0 or w == 0:
                tabela[i][w] = 0
            elif pesos[i-1] <= w:
                tabela[i][w] = max(valores[i-1] + tabela[i-1][w-pesos[i-1]], tabela[i-1][w])
            else:
                tabela[i][w] = tabela[i-1][w]
 
    # Retorna a solução
    return tabela[n][capacidade]
