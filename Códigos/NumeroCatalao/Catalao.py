def catalan(n):
    # Inicializa a tabela com 0's
    table = [0] * (n+1)

    # O caso base é C(0) = 1
    table[0] = 1

    # Preenche a tabela usando a fórmula de Bellman
    for i in range(1, n+1):
        for j in range(i):
            table[i] += table[j] * table[i-j-1]

    # Retorna o valor de C(n)
    return table[n]

# Teste
n = int(input("Digite o valor de n: "))
print("C({}) = {}".format(n, catalan(n)))
