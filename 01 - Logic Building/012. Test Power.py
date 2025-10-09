# Dados dois números positivos x e y, verifique se y é uma potência de x ou não.

import math

def naive_approach(x: int, y: int) -> bool:
    if x == 1: # 1 elevado a qualquer número é sempre 1
        return y == 1

    aux = 1
    while aux < y:
        aux *= x

    return aux == y

def expected_approach(x: int, y: int) -> bool:
    aux = math.log(y) / math.log(x)
    return aux == math.floor(aux)

if __name__ == "__main__":
    print("Teste de Potência")
    x, y = 2, 128
    print(f"{y} é uma potência de {x}?")
    print("Abordagem Simples:", naive_approach(x, y))
    print("Abordagem Esperada:", expected_approach(x, y))

    # Abordagem Simples - Tempo(log_x(y)), Espaço(1)
    # Abordagem Esperada - Tempo(1), Espaço(1)
