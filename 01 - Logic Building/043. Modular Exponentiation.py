#---------------------------------------------------------------------------------
# Exponenciação Modular
#---------------------------------------------------------------------------------
# Dados três inteiros x, n e M, calcule (x^n) % M (o resto quando x elevado para a
# potência n é dividido por M).

#---------------------------------------------------------------------------------
# Abordagem Simples - Usando as Funções do Python
#---------------------------------------------------------------------------------
def naive_approach(x: int, n: int, M: int) -> int:
    return (x ** n) % M

#---------------------------------------------------------------------------------
# Abordagem Alternativa - Métod* da Multiplicação Repetida
#---------------------------------------------------------------------------------
def alternative_approach(x: int, n: int, M: int) -> int:
    """
    Abordagem Alternativa - Tempo O(n), Espaço O(1)
    """
    res = 1
    for _ in range(n):
        res = res * x % M

    return res

#---------------------------------------------------------------------------------
# Abordagem Esperada - Usando Exponenciação Binária
#---------------------------------------------------------------------------------
# * Start with the result as 1.
# * Use a loop that runs while the exponent n is greater than 0.
# * If the current exponent is odd, multiply the result by the current base and apply the modulo.
# * Square the base and take the modulo to keep the value within bounds.
# * Divide the exponent by 2 (ignore the remainder).
# * Repeat the process until the exponent becomes 0.
def expected_approach(x: int, n: int, M: int) -> int:
    """
    Abordagem Esperada - Tempo O(log(n)), Espaço O(1)
    """
    res = 1

    while n > 0:
        if n % 2 == 1:
            res = (res * x) % M
            n -= 1
        else:
            x = (x * x) % M
            n //= 2

    return res


if __name__ == "__main__":
    print("Exponenciação Modular")
    x, n, M = 2, 6, 10
    print("Abordagem Simples:", naive_approach(x, n, M))
    print("Abordagem Alternativa:", alternative_approach(x, n, M))
    print("Abordagem Esperada:", expected_approach(x, n, M))
