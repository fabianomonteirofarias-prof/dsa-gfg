def fatorial(n: int) -> int:
    f = 1
    while n:
        f *= n
        n -= 1

    return f

def naive_approach(n: int, r: int) -> int:
    return fatorial(n) // fatorial(n - r)

if __name__ == "__main__":
    print("Compute nPr")
    n, r = 6, 3
    print("Abordagem Simples:", naive_approach(n, r))
    # Abordagem Simples - Tempo O(n), Espaço O(1)
