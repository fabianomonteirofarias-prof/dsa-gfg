# Dado dois inteiros positivos a e b, encontre o MDC dos dois números.
# Nota: O MDC (Maior Divisor Comum) ou MFC (Maior Fator Comum) de dois
# números é o maior número capaz de divide eles.

def approach_1(a: int, b: int) -> int:
    m = min(a, b)

    while m > 0:
        if a % m == 0 and b % m == 0:
            return m

        m -= 1

    return m


def approach_2(a: int, b: int) -> int:
    while (a != b):
        if a > b:
            a -= b
        else:
            b -= a

    return a


def approach_3(a: int, b: int) -> int:
    while b != 0:
        aux = a
        a = b
        b = aux % b

    return a


if __name__ == "__main__":
    print("Maior Divisor Comum")

    # a, b = 12, 15
    a, b = 20, 28

    print("Abordagem 1:", approach_1(a, b))
    print("Abordagem 2:", approach_2(a, b))
    print("Abordagem 3:", approach_3(a, b))

    # Abordagem 1 - Tempo(min(a,b)), Espaço(1)
    # Abordagem 2 - Tempo(min(a,b)), Espaço(1)
    # Abordagem 3 - Tempo(log(min(a, b))), Espaço(1)