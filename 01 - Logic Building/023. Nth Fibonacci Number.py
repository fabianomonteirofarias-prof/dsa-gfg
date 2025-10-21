# Given a positive integer n, the task is to find the nth Fibonacci number.
# The Fibonacci sequence is a sequence where the next term is the sum of the
# previous two terms. The first two terms of the Fibonacci sequence are 0
# followed by 1. The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21.

def recursive_approach(n: int) -> int:
    if n <= 1:
        return n

    return recursive_approach(n - 1) + recursive_approach(n - 2)

def memorization_approach(n: int) -> int:
    def util(n: int, memo: list) -> int:
        if n <= 1:
            return n

        if memo[n] != -1:
            return memo[n]

        memo[n] = util(n - 1, memo) + util(n - 2, memo)

        return memo[n]

    # create a memorization table
    memo = [-1] * (n+1)
    # call the util function
    return util(n, memo)

def bottomUp_approach(n: int) -> int:
    # handle the edge case
    if n <= 1:
        return n
    # create a list to store the fibonacci numbers
    dp = [0] * (n+1)
    # inicialize the first two fibonacci numbers
    dp[0], dp[1] = 0, 1
    # fill the list iteratively
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    # return the nth fibonacci number
    return dp[n]

def spaceOtimized_approach(n: int) -> int:
    if n <= 1:
        return n

    curr = 0

    prev1 = 0
    prev2 = 1

    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr

    return curr

def matrix_approach(n: int) -> int:
    def multiply(matrix1: list, matrix2: list):
        x = matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0]
        y = matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]
        z = matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]
        w = matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]
        # update matrix1
        matrix1[0][0], matrix1[0][1] = x, y
        matrix1[1][0], matrix2[1][1] = z, w

    def matrix_power(matrix1: list, n: int):
        if n == 0 or n == 1:
            return
        # inicialize helper matrix
        matrix2 = [[1, 1], [1, 0]]

        # matrix1^(n//2) recursive
        matrix_power(matrix1, n // 2)
        # square matrix1
        multiply(matrix1, matrix1)

        if n % 2 != 0:
            multiply(matrix1, matrix2)

    # function to calculate the nth fibonacci number
    if n <= 1:
        return n

    # inicialize the transformation matrix
    matrix1 = [[1, 1], [1, 0]]

    matrix_power(matrix1, n-1)

    return matrix1[0][0]

if __name__ == "__main__":
    print("Nth Número de Fibonacci")
    n = 8
    print("Abordagem Recursiva:", recursive_approach(n))
    print("Abordagem de Memorização:", memorization_approach(n))
    print("Abordagem Bottom-Up:", bottomUp_approach(n))
    print("Abordagem de Espaço Otimizada:", spaceOtimized_approach(n))
    print("Abordagem com Matrizes:", matrix_approach(n))

    # Abordagem Recursiva - Tempo(2^n), Espaço(n)
    # Abordagem Memorização - Tempo(n), Espaço(n)
    # Abordagem Bottom Up - Tempo(n), Espaço(n)
    # Abordagem de Espaço Otimizado - Tempo(n), Espaço(1)
    # Abordagem com Matrizes - Tempo(log(n)), Espaço(log(n))
