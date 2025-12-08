#--------------------------------------------------------------------------------
# Triângulo de Pascal
#--------------------------------------------------------------------------------
# Dado um inteiro n, a tarefa é encontrar os primeiros n linhas
# do triângulo de pascal. O Triângulo de Pascal é um array de
# coeficientes binomiais.

#--------------------------------------------------------------------------------
# Abordagem Simples - Utilizando o Coeficiente Binomial
#--------------------------------------------------------------------------------

def binomialCoeff(n: int, k: int) -> int:
    #
    # Calcula o Coeficiênte Binomial - Tempo O(n), Espaço (1)
    #
    res = 1
    if k > n - k:
        k = n - k

    for i in range(k):
        res *= (n - i)
        res //= (i + 1)

    return res

def naive_approach(n: int) -> list:
    """
    Abordagem Simples - Tempo O(n^3), Espaço O(1)
    """
    mat = []

    for row in range(n):
        arr = []
        for i in range(row+1):
            arr.append(binomialCoeff(row, i))
        mat.append(arr)

    return mat


#--------------------------------------------------------------------------------
# Abordagem Esperada - Utilizando Programação Dinâmica
#--------------------------------------------------------------------------------

def expected_approach(n: int) -> list:
    """
    Abordagem Esperada - Tempo O(n^2), Espaço O(n^2)
    """
    mat = []

    for row in range(n):
        arr = []
        for i in range(row+1):
            if row == i or i == 0:
                arr.append(1)
            else:
                arr.append(mat[row - 1][i - 1] + mat[row - 1][i])

        mat.append(arr)

    return mat

#--------------------------------------------------------------------------------
# Abordagem Esperada - Utilizando Coeficiente Binomial e Otimizando Espaço
#--------------------------------------------------------------------------------
def alternative_approach(n: int) -> list:
    """
    Abordagem Alternativa - Tempo O(n^2), Espaço O(1)
    """
    mat = []
    for row in range(1, n + 1):
        arr = []
        c = 1
        for i in range(1, row + 1):
            arr.append(c)
            c = c * (row - i) // i
        mat.append(arr)

    return mat


if __name__ == "__main__":
    print("Triângulo de Pascal")
    n = 6
    print("Abordagem Simples:", naive_approach(n))
    print("Abordagem Esperada:", expected_approach(n))
    print("Abordagem Esperada (Alternativa):", alternative_approach(n))
