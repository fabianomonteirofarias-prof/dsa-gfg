# Dado um número n, encontre a soma de seus dígitos.

def convertion_approach(n: int) -> int:
    return sum([int(s) for s in str(n)])

def iterative_approach(n: int) -> int: # soma
    s = 0 # soma
    while n != 0:
        last = n % 10
        s += last
        n //= 10

    return s

def recursion_approach(n: int) -> int:
    if n == 0:
        return 0

    last = n % 10

    return last + recursion_approach(n // 10)

if __name__ == "__main__":
    print("Soma dos Dígitos")
    n = 123456789
    print("Abordagem com Conversão:", convertion_approach(n))
    print("Abordagem Iterativa:", iterative_approach(n))
    print("Abordagem Recursiva:", recursion_approach(n))

    # Abordagem com Conversão - Tempo(d), Espaço(d) | Obs.: d = qntd de dígitos ≈ log_10(n).
    # Abordagem Iterativa - Tempo(log_10(n)) - Espaço(1)
    # Abordagem Recursiva - Tempo(log_10(n)), Espaço(log_10(n))