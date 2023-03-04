import sys

def matrix_multiplication(A, B):
    n = len(A)
    m = len(B[0])
    mids = len(A[0])

    # Inicializa a matriz C com zeros
    C = [[0] * m for _ in range(n)]

    # Calcula o valor de cada célula de C
    for i in range(n):
        for j in range(m):
            C[i][j] = sys.maxsize
            for k in range(mids):
                cost = A[i][k] + B[k][j]
                if cost < C[i][j]:
                    C[i][j] = cost

    return C

# Recebe as dimensões das matrizes
dim_A = input("Digite as dimensões da matriz A separadas por espaço: ")
dim_A = [int(x) for x in dim_A.split()]
dim_B = input("Digite as dimensões da matriz B separadas por espaço: ")
dim_B = [int(x) for x in dim_B.split()]

# Verifica se as dimensões são compatíveis para multiplicação
if dim_A[1] != dim_B[0]:
    print("As dimensões informadas não são compatíveis para multiplicação.")
    exit()

# Recebe os valores das matrizes
A = []
B = []

print("Digite os valores da matriz A:")
for i in range(dim_A[0]):
    row = input().split()
    A.append([int(x) for x in row])

print("Digite os valores da matriz B:")
for i in range(dim_B[0]):
    row = input().split()
    B.append([int(x) for x in row])

# Multiplica as matrizes
C = matrix_multiplication(A, B)

# Imprime a matriz resultante
print("A x B =")
for row in C:
    print(row)
