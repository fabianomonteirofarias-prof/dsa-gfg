# Dado n, conte todos 'a' e 'b' que satisfaz a condição
# a^3 + b^3 = n. Onde (a, b) e (b, a) são consideradas
# dois pares diferentes.

def naive_approach(n: int) -> int:
    count = 0

    for a in range(1, n+1):
        for b in range(n+1):
            if a ** 3 + b ** 3 == n:
                count += 1

    return count

def expected_approach(n: int) -> int:
    count = 0

    for i in range(1, int(pow(n, 1/3)) + 1):
        cube_number = i * i * i
        diff = n - cube_number

        cb_diff = round(diff ** (1/3))

        if cb_diff * cb_diff * cb_diff == diff:
            count += 1

    return count

if __name__ == "__main__":
    print("Contagem de Cubos de Pares")
    n = 28
    print("Abordagem Simples:", naive_approach(n))
    print("Abordagem Esperada:", expected_approach(n))

    # Abordagem Simples - Tempo(n^2), Espaço(1)
    # Abordagem Esperada - Tempo(n^1/3), Espaço(1)
