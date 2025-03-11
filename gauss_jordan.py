# gauss_jordan.py  

def print_matrix(M, decimal = 3):
    for row in M:
        print([round(x, decimal) + 0 for x in row])

def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
    return M

matriz_zeros = zeros_matrix(3, 3)
print_matrix(matriz_zeros)

def GaussJordanMethod(augMat):
    n = len(augMat)
    m = len(augMat[0])
    #print(n)
    #print(m)

    for i in range(n):
    # Verificar se o pivo pode ser definido ou não
        print(augMat)
        if augMat[i][i] == 0:
            for j in range(i + 1, n):
                augMat[i], augMat[j] = augMat[j], augMat[i]
                break
        else:
            # Caso não encontre linha com valor diferente de zero
            # Temos um singularidade
            raise ValueError("Matriz singular!")
        print(augMat, '\n')

    # Normalizando cada linha
    # L_i <-- L_i/a_ii
        if augMat[i][i] != 1:
            divisor = augMat[i][i]
            for k in range(m):
                augMat[i][k] /= divisor
        else:
            pass

        # Zerando as entradas do pivo
        # L_i <-- L_j - a_ji * L_i
        for j in range(n):
            if i != j:
                coef = augMat[j][i]
                for k in range(m):
                    augMat[j][k] -= coef * augMat[i][k]
            else:
                pass
        
    print_matrix(augMat)

    if i == 0:
        print(divisor)
        print(augMat[0])


#matrix = [[3.0, 2.0, -4.0, 3.0], [2.0, 3.0, 3.0, 15.0], [5.0, -3.0, 1.0, 14.0]]
matrix = [[0, 2, 0, 1, 0], [2, 2, 3, 2, -2], [4, -3, 0, 1, -7], [4, -3, 0, 1, -7], [6, 1, -6, -5, 6]]
# print(matrix)

GaussJordanMethod(matrix)