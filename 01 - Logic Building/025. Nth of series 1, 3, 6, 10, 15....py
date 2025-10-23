# Given a number n, find the n-th term in the series 1, 3, 6, 10, 15, 21...

def naive_approach(n: int) -> int:
    res = 0
    while n > 0:
        res += n
        n -= 1

    return res

def expected_approach(n: int) -> int:
    return n * (n+1)//2

if __name__ == "__main__":
    print("Enésimo número da sequência: 1, 3, 6, 10, 15...")
    n = 6
    print("Abordagem Simples:", naive_approach(n))
    print("Abordagem Esperada:", expected_approach(n))

    # Abordagem Simples - Tempo(n), Espaço(1)
    # Abordagem Esperada - Tempo(1), Espaço(1)
