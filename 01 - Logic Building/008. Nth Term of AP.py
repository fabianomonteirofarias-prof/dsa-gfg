# Dado dois inteiros a1 e a2, o primeiro e o segundo termo
# de uma Serie Aritmetica respectivamente, o problema é
# encontrar o nth termo da série.

def naive_approach(a1: int, a2: int, n: int) -> int:
    nthTerm = a1 # nth
    d = a2 - a1 # diferença

    for _ in range(1, n):
        nthTerm += d

    return nthTerm

def expected_approach(a1: int, a2: int, n: int) -> int:
    return (a2 - a1) * (n - 1) + a1


if __name__ == "__main__":
    print("Enésimo Termo de uma PA")

    a1, a2, n = 1, 3, 10

    print("Abordagem Simples: ", naive_approach(a1, a2, n))
    print("Abordagem Esperada: ", expected_approach(a1, a2, n))

    # Abordagem Simples - Tempo(n), Espaço(1)
    # Abordagem Esperada - Tempo(1), Espaço(1)
