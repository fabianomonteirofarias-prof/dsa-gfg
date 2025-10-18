# Dadas duas matrizes inteiras a[] e b[] contendo dois inteiros,
# cada uma representando o numerador e o denominador de uma fração,
# respetivamente. A tarefa é encontrar a soma das duas frações e
# retornar o numerador e o denominador do resultado.

#----------------------------------------------------------------
# Auxiliar Functions
#----------------------------------------------------------------
def greater_common_divisor(a: int, b: int) -> int:
    # Tempo(log(min(a, b))), Espaço(1)
    while b != 0:
        a, b = b, a % b

    return a

def least_common_multiple(a: int, b: int) -> int:
    # Tempo(log(min(a, b))), Espaço(1)
    gcd = greater_common_divisor(a, b)

    return a * b // gcd
#----------------------------------------------------------------

def expected_approach(a: list, b: list) -> list:
    # find least common multiple - the result's denominator
    denominator = least_common_multiple(a[1], b[1])

    # find the multiples of the denominators
    a_mult, b_mult = denominator // a[1], denominator // b[1]

    # sum the numerators
    numerator = a_mult * a[0] + b_mult * b[0]

    # find simple form by find greater common divisor
    gcd = greater_common_divisor(numerator, denominator)

    return [numerator // gcd, denominator // gcd]

if __name__ == "__main__":
    print("Soma de Duas Frações")
    a, b = [1, 2], [3, 2]
    print("Abordagem Simples:", expected_approach(a, b))
    a, b = [1, 3], [3, 9]
    print("Abordagem Simples:", expected_approach(a, b))
    a, b = [1, 5], [3, 15]
    print("Abordagem Simples:", expected_approach(a, b))

    # Abordagem Esperada: Tempo(Log(min(a, b))), Espaço(1)
