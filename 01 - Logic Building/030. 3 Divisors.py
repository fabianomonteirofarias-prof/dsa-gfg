# Dado um número n, mostre a contagem de números de 1 a n que possuem exatos 3 divisores.

def naive_approach(n: int) -> int:
    count = 1

    for i in range(5, n+1):
        aux_count = 1

        for j in range(2, i+1):
            if i % j == 0:
                aux_count += 1

        if aux_count == 3:
            count += 1

    return count

def expected_approach(n: int) -> int:
    def is_prime(x: int) -> bool:
        for i in range(2, int(x ** 0.5)+1):
            if x % i == 0:
                return False
        return True

    count = 0
    for i in range(2, int(n ** 0.5)+1):
        if is_prime(i):
            count += 1

    return count

if __name__ == "__main__":
    print("3 Divisores")
    n = 20
    print("Abordagem Simples:", naive_approach(n))
    print("Abordagem Esperada:", expected_approach(n))

    # Abordagem Simples - Tempo(n^2), Espaço(1)
    # Abordagem Esperado - Tempo(n^¾)