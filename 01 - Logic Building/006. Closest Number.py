# Dado dois inteiros n e m (m != 0). Encontre o número mais perto
# de n e divisível por m. Se houver mais que um número, então
# retorne com o maior valor absoluto.

def naive_approach(n: int, m: int) -> int:
    closest = 0
    min_difference = float('inf')
    for i in range(n - abs(m), n + abs(m) + 1):
        if i % m == 0:
            difference = abs(n-i)
            if difference < min_difference or \
                    (difference == min_difference and abs(i) > abs(closest)):
                min_difference = difference
                closest = i

    return closest

def expected_approach(n: int, m: int) -> int:
    q = int(n / m)

    # primeiro
    n1 = q * m

    # segundo
    if q > 0:
        n2 = m * (q + 1)
    else:
        n2 = m * (q - 1)

    if abs(n-n1) < abs(n-n2):
        return n1

    return n2


if __name__ == "__main__":
    print("Número Mais Próximo de N e Divisível por M")
    n, m = -15, 6
    print("Abordagem Simples: ", naive_approach(n, m))
    print("Abordagem Esperada: ", expected_approach(n, m))

    # Abordagem Simples - Tempo(m), Espaço(1)
    # Abordagem Esperada - Tempo(1), Espaço(1)
