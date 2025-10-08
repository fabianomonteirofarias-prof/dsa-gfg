# Dado um número inteiro positivo, verifique se um
# número é primo ou não. Um primo é natural maior
# que 1 que não é divisível por outros que 1 e ele
# mesmo. Exemplos dos primeiros números primos são
# {2, 3, 5, ...}

import math

def naive_approach(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def alternative_approach(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def expected_approach(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False

    return True


if __name__ == "__main__":
    print("Teste dos Números Primos")

    # Lista de teste
    test_list = range(1, 10)
    for n in test_list:
        print("Número:", n)
        print("Abordagem Simples:", "Primo." if naive_approach(n) else "Não é primo.")
        print("Abordagem Alternativa:", "Primo." if alternative_approach(n) else "Não é primo.")
        print("Abordagem Esperada:", "Primo." if expected_approach(n) else "Não é primo.")
        print("--------------")

    # Abordagem Simples - Tempo(n), Espaço(1)
    # Abordagem Alternativa:  Tempo(sqrt(n)), Espaço(1)
    # Abordagem Esperada: Tempo(sqrt(n)), Espaço(1)