#------------------------------------------------------------------------------------------
# Todos os Fatores de um Número
#------------------------------------------------------------------------------------------
# Dado um número inteiro positivo n, encontre todos os divisores distintos de n.

#------------------------------------------------------------------------------------------
# Abordagem Simples - Iterando sobre todos os números
#------------------------------------------------------------------------------------------
def naive_approach(n: int) -> list:
    """
    Abordagem Simples - Tempo O(n), Espaço O(1)
    """
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors

#------------------------------------------------------------------------------------------
# Abordagem Esperada - Encontrando os fatores em pares
#------------------------------------------------------------------------------------------
import math

def expected_approach(n: int) -> list:
    """
    Abordagem Esperada - Tempo O(sqrt(n)), Espaço O(1)
    """
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if n // i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(n // i)
    return divisors

if __name__ == "__main__":
    print("Todos os Fatores")
    n = 100
    print("Abordagem Simples:", naive_approach(n))
    print("Abordagem Esperada:", expected_approach(n))
