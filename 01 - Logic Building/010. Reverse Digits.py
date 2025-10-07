# Dado um inteiro n, encontro o inverso dos seus dígitos.

def convertion_approach(n: int) -> int:
    return int(str(n)[::-1])

def convertion_alternative_approach(n: int) -> int:
    r = list(str(n))
    r.reverse()

    return int(''.join(r))

def iterative_approach(n: int) -> int:
    aux = 0
    while n != 0:
        aux *= 10
        aux += n % 10
        n //= 10

    return aux

def recursive_approach(n: int, aux1: list, aux2: list):
    if n > 0:
        recursive_approach(n // 10, aux1, aux2)
        aux1[0] += (n % 10) * aux2[0]
        aux2[0] *= 10

if __name__ == "__main__":
    print("Inversão dos Dígitos")
    n = 123456789
    print("Abordagem com Conversão:", convertion_approach(n))
    print("Abordagem com Conversão Alternativa:", convertion_alternative_approach(n))
    print("Abordagem Iterativa:", iterative_approach(n))

    revNum = [0]
    basePos = [1]
    recursive_approach(n, revNum, basePos)
    print("Abordagem Recursiva:", revNum[0])

    # Abordagem com Conversão - Tempo(log n), Espaço(1)
    # Abordagem com Conversão Alternativa - Tempo(log n), Espaço(log n)
    # Abordagem Iterativa - Tempo(log n), Espaço(1)
    # Abordagem Iterativa - Tempo(log n), Espaço(log n)