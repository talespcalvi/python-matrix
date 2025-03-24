def solve_gauss_jordan(augMat, decimals=3):
    def determinant(AM):
        n = len(AM)
        for fd in range(n):
            if AM[fd][fd] == 0:
                for j in range(fd + 1, n):
                    if AM[j][fd] != 0:
                        AM[fd], AM[j] = AM[j], AM[fd]
                        break
                else:
                    raise ValueError("Matriz singular!")

            for i in range(fd + 1, n):
                crScaler = AM[i][fd] / AM[fd][fd]
                for j in range(n):
                    AM[i][j] -= crScaler * AM[fd][j]

        product = 1.0
        for i in range(n):
            product *= AM[i][i]
        return product

    def verifica_non_singularidade(A):
        det = determinant([row[:] for row in A])
        if det == 0:
            raise ArithmeticError("Matriz Singular!")

    verifica_non_singularidade([row[:-1] for row in augMat])

    n = len(augMat)
    m = len(augMat[0])

    for i in range(n):
        if augMat[i][i] == 0:
            for j in range(i + 1, n):
                if augMat[j][i] != 0:
                    augMat[i], augMat[j] = augMat[j], augMat[i]
                    break
            else:
                raise ValueError("Matriz singular!")

        divisor = augMat[i][i]
        for k in range(m):
            augMat[i][k] /= divisor

        for j in range(n):
            if i != j:
                coef = augMat[j][i]
                for k in range(m):
                    augMat[j][k] -= coef * augMat[i][k]

    solutions = [round(row[-1], decimals) for row in augMat]
    print("Solução:", solutions)
    return solutions

# Exemplo de uso:
#matrix = [[3.0, 2.0, -4.0, 3.0], [2.0, 3.0, 3.0, 15.0], [5.0, -3, 1.0, 14.0]]
matrix = [[2, 2, -3, 4],
          [1, 3, 1, 11],
          [2, 5, -4, 13]]
solve_gauss_jordan(matrix)
