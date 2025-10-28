# Dado um inteiro positivo n, encontre sua raiz quadrada. Se n não possui raiz perfeita, então retorne √n arredondado;

def naive_approach(n: int) -> int:
    res = 1

    while res * res <= n:
        res += 1

    return res - 1

def expected_approach(n: int) -> int:
    lo = 1
    hi = n
    res = 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if mid * mid <= n:
            lo = mid + 1
            res = mid

        else:
            hi = mid - 1

    return res

def alternative_approach(n: int) -> int:
    return int(n ** (1/2))

import math

def formula_approach(n: int) -> int:
    res = int(math.exp(1/2 * math.log(n)))
    if (res + 1) ** 2 <= n:
        res += 1

    return res

if __name__ == "__main__":
    print("Raiz Quadrada")
    # n = 4
    n = 50
    print("Abordagem Simples:", naive_approach(n))
    print("Abordagem Esperada:", expected_approach(n))
    print("Abordagem Alternativa:", alternative_approach(n))
    print("Abordagem Usando a Formula:", formula_approach(n))

    # Abordagem Simples - Tempo(√n), Espaço(1)
    # Abordagem Esperada - Tempo(log(n)), Espaço(1)
    # Abordagem Alternativa - Tempo(log(n)), Espaço(1)
    # Abordagem Formula - Tempo(1), Espaço(1)
