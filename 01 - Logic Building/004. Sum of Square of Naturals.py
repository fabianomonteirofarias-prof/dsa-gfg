# Dado um inteiro positivo n, encontre a soma dos quadrados dos primeiros n números naturais.

def naive_approach(n: int) -> int:
    return sum([i ** 2 for i in range(1, n+1)])

def alternative_approach_for(n: int) -> int:
    s:int = 1 # soma
    for i in range(2, n+1):
        s += i * i

    return s

def alternative_approach_while(n: int) -> int:
    s:int = 1 # soma
    i:int = 2 # contador
    while i < (n + 1):
        s += i * i
        i += 1

    return s

def recursive_approach(n: int) -> int:
    if n == 1:
        return 1

    return n*n + recursive_approach(n-1)

def expected_approach(n: int) -> int:
    return (n * (n + 1) // 2) * (2 * n + 1) // 3

if __name__ == "__main__":
    print("Soma dos Quadrados dos Primeiros 'n' Números Naturais")

    # lista de teste
    test_list = range(1, 11)

    print("Abordagens")
    print("Simples", "|", "Alternativa (for)", "|", "Alternativa (while)", "|", "Recursiva", "|", "Esperada")
    for n in test_list:
        print(naive_approach(n), "|",
              alternative_approach_for(n), "|",
              alternative_approach_while(n), "|",
              recursive_approach(n), "|",
              expected_approach(n))

    # Abordagens
    # Simples - Tempo(n), Espaço(1)
    # Alternativo (for) - Tempo(n), Espaço(1)
    # Alternativo (while) - Tempo(n), Espaço(1)
    # Recursivo - Tempo(n), Espaço(n)
    # Esperado - Tempo(1), Espaço(1)
