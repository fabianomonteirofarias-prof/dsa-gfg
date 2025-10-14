# Dado um inteiro positivo a e b, Encontre o Menor Múltiplo Comum de a e b.
# MMC de dois números é o menores número que pode dividir ambos os números.

def naive_approach(a: int, b: int) -> int: # naive approach
    aux1 = max(a, b) # greater
    aux2 = min(a, b) # least

    for i in range(aux1, a * b + 1, aux1):
        if i % aux2 == 0:
            return i

    return a * b

def expected_approach(a: int, b: int) -> int: # expected approach
    temp_a = a
    temp_b = b

    # GCD
    while temp_b != 0:
        aux = temp_a
        temp_a = temp_b
        temp_b = aux % temp_b

    return a * b // temp_a


if __name__ == "__main__":
    print("Menor Múltiplo Comum")
    a, b = 5, 10
    # a, b = 5, 11
    # a, b = 12, 20

    print("Abordagem Simples:", naive_approach(a, b))
    print("Abordagem Esperada:", expected_approach(a, b))

    # Abordagem Simples - Tempo(min(a, b)), Espaço(1)
    # Abordagem Esperada - Tempo(log(min(a, b))), Espaço(1)