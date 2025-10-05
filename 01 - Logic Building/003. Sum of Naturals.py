# Dado um número inteiro positivo n, encontre a soma dos primeiros n números naturais.

def naive_approach(n: int) -> int:
    return sum(range(1, n+1))

def alternative_approach(n: int) -> int: # usando o for
    s:int = 0   # soma
    for i in range(1, n +1):
        s += i

    return s

def another_alternative_approach(n: int) -> int: # usando while
    s:int = 0   # soma
    i:int = 1
    while i < n+1:
        s += i
        i += 1

    return s

def recursive_approach(n: int) -> int:
    if n == 1:
        return 1

    return n + recursive_approach(n-1)

def expected_approach(n: int) -> int:
    return int(n * (n+1) // 2)


if __name__ == "__main__":
    print("Soma dos Números Naturais")

    # lista de números para teste
    test_list = range(1, 11)

    print("Abordagens")
    print("Simples" ,"|", "Alternativa (for)", "|", "Alternativa (while)", "|", "Recursiva", "|", "Esperada")
    for i in test_list:
        print(naive_approach(i), "|", alternative_approach(i), "|", another_alternative_approach(i), "|", recursive_approach(i),"|", expected_approach(i))

    # Abordagem Simples - Tempo(?). Espaço(?)
    # Abordagem Alternativa (for), Tempo(n), Espaço(1)
    # Abordagem Alternativa (while), Tempo(n). Espaço(1)
    # Abordagem Recursiva - Tempo(n), Espaço(n)
    # Abordagem Esperada - Tempo(1), Espaço(1)