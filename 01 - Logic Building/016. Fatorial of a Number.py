# Dado u número inteiro não negativo n, calcule o fatorial do número dado.
# Nota: Fatorial de n é definido como n * (n - 1) * (n - 2) * ... * 1, para n = 0 é 1.
# Given the non-negative integers n , compute the factorial of a given number.
# Note: Factorial of n is defined as n * (n -1) * (n - 2) * ... * 1, for n = 0, factorial is 1.

def iterative_for_approach(n: int) -> int:
    if n == 0: return 1

    mult = n
    for i in range(2, n):
        mult *= i
    return mult

def iterative_while_approach(n: int) -> int:
    if n == 0: return 1

    mult = n
    i = n - 1
    while i > 0:
        mult *= i
        i -= 1
    return mult

def recursive_approach(n: int) -> int:
    if n == 1 or n == 0:
        return 1

    return n * recursive_approach(n - 1)

def expected_approach(n: int) -> int: ...

if __name__ == "__main__":
    print("Fatorial de um Número")
    n = 5
    print("Abordagem Iterativa (for):", iterative_for_approach(n))
    print("Abordagem Iterativa (while):", iterative_while_approach(n))
    print("Abordagem Recursiva:", recursive_approach(n))

    # Abordagem Iterative (for & while) - Tempo(n), Espaço(1)
    # Abordagem Recursiva - Tempo(n), Espaço(n)