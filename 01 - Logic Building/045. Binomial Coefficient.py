#------------------------------------------------------------------------
# Coeficiente Binomial
#------------------------------------------------------------------------
# Dados valores inteiros n e k, a tarefa é encontrar o valor do
# Coeficiente Binomial C(n, k).
#
# * Um coeficiente binomial C(n, k) pode ser definido como o coeficiente
# de x^k na expansão de (1 + x)^n.
# * Um coeficiente binomial C(n, k) também fornece o número de maneiras,
# desconsiderando a ordem, que k objetos podem ser escolhidos entre n
# objetos. Mais formalmente, o número de subconjuntos de elementos k
# (ou combinações k) de um conjunto de n elementos.

#------------------------------------------------------------------------
# Abordagem Recursiva
#------------------------------------------------------------------------
def recursive_approach(n: int, k: int):
    """
    Abordagem Recursiva - Tempo O(2^n), Espaço O(n)
    """
    if k > n:
        return 0

    if k == 0 or k == n:
        return 1

    return recursive_approach(n - 1, k - 1) + recursive_approach(n - 1, k)


#------------------------------------------------------------------------
# Abordagem Memoization - Top-Down
#------------------------------------------------------------------------
def getnCk(n: int, k: int, memo: list):
    if k > n:
        return 0

    if k == 0 or k == n:
        return 1

    if memo[n][k] != -1:
        return memo[n][k]

    memo[n][k] = getnCk(n-1, k-1, memo) + getnCk(n-1, k, memo)
    return memo[n][k]

def memoization_approach(n: int, k: int) -> int:
    """
    Abordagem Memoization - Tempo O(n * k), Espaço O(n * k)
    """
    memo = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]
    return getnCk(n, k, memo)


#------------------------------------------------------------------------
# Abordagem Tabulação - Bottom-Up
#------------------------------------------------------------------------
def tabulation_approach(n: int, k: int) -> int:
    """
    Abordagem Tabulação - Tempo O(n * k), Espaço O(n * k)
    """
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][k]

#------------------------------------------------------------------------
# Abordagem Tabulação Otimizado - Bottom-Up
#------------------------------------------------------------------------
def optimized_tabulation_approach(n: int, k: int) -> int:
    """
    Abordagem de Tabulação com Espaço Otimizado - Tempo O(n * k), Espaço O(k)
    """
    dp = [0] * (k + 1)

    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            dp[j] = dp[j] + dp[j - 1]

    return dp[k]


if __name__ == "__main__":
    print("Coeficiente Binomial")
    n, k = 10, 5
    print("Abordagem Recursiva:", recursive_approach(n, k))
    print("Abordagem Memoization:", memoization_approach(n, k))
    print("Abordagem Tabulação:", tabulation_approach(n, k))
    print("Abordagem Otimizada:", optimized_tabulation_approach(n, k))
