# Dado três números a, b e k, encontre o k-ésimo digito em a^b do lado direito.

def naive_approach(a: int, b: int, k: int) -> int:
    aux = a ** b
    res = 0

    while k:
        res = aux % 10
        aux //= 10
        k -= 1

    return res

def alternative_approach(a: int, b: int, k: int) -> int:
    mod = 10 ** k
    res = 1
    base = a

    while b > 0:
        if b & 1:
            res = (res * base) % mod
        base = (base * base) % mod
        b >>= 1

    for i in range(1, k):
        res //= 10
    return res

def string_approach(a: int, b: int, k: int) -> int:
    s = str(a ** b)
    return int(s[-k]) if k <= len(s) else 0

if __name__ == "__main__":
    print("K-ésimo número de a^b")
    a, b, k = 5, 2, 2
    print("Abordagem Simples:", naive_approach(a, b, k))
    print("Abordagem Alternativa:", alternative_approach(a, b, k))
    print("Abordagem com String:", string_approach(a, b, k))

    # Abordagem Simples - Tempo O(k), Espaço O(1)
    # Abordagem Alternativa - Tempo O(log(b)), Espaço O(1)
    # Abordagem com String - Tempo O(1), Espaço 0 (1)