#-----------------------------------------------------------
# Crivo de Eratosthenes
#-----------------------------------------------------------
# Dado um número n, encontre todos os números primos menores
# ou iguais a n.

#-----------------------------------------------------------
# Abordagem Simples
#-----------------------------------------------------------
def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i<= n:
        if n % i == 0 or n % (i+2) == 0:
            return False

        i += 6

    return True

def naive_approach(n: int) -> list:
    """
    Abordagem Simples - Tempo O(n * sqrt(n)), Espaço O(1)
    """
    arr = []
    for i in range(n):
        if is_prime(i):
            arr.append(i)

    return arr


#-----------------------------------------------------------
# Abordagem Esperada
#-----------------------------------------------------------
def expected_approach(n: int) -> list:
    """
    Abordagem Esperada - Tempo O(n * log(log(n))), Espaço O(n)
    """
    prime = [True] * (n +1)

    p = 2

    while p*p <= n:
        if prime[p]:
            for i in range(p * p, n+1, p):
                prime[i] = False

        p += 1

    res = []
    for p in range(2, n + 1):
        if prime[p]:
            res.append(p)

    return res


if __name__ == "__main__":
    print("Crivo de Eratosthenes")
    n = 100
    print("Abordagem Simples:", naive_approach(n))
    print("Abordagem Esperada:", expected_approach(n))
