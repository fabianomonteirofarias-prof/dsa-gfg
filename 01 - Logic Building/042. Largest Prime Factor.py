#------------------------------------------------------------------------------------------------
# Maior Fator Primo
#------------------------------------------------------------------------------------------------
# Dado um inteiro positivo n (1 <= n <= 10^15). Encontre o maior fator primo desse número.

#------------------------------------------------------------------------------------------------
# Abordagem Simples - Divisão Básica por Tentativa
#------------------------------------------------------------------------------------------------
# * O métod* começa removendo todos os fatores de 2, pois é o único primo par.
# * Uma vez que o 2 é completamente removido, os números ímpares são verificados a partir do 3.
# * Cada número ímpar é testado quanto à divisibilidade, e o número é dividido repetidamente até
# que o fator seja totalmente removido. Esse processo continua para todos os números ímpares até √n.
# * Se um número maior que 2 permanecer após todas as divisões, ele é um número primo e o maior
# fator primo.
def naive_approach(n: int) -> int:
    """
    Abordagem Simples - Tempo O(sqrt(n)), Espaço O(1)
    """
    largestPrime = -1

    while n % 2 == 0:
        largestPrime = 2
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            largestPrime = i
            n //= i
        i += 2

    if n > 2:
        largestPrime = n

    return largestPrime

#------------------------------------------------------------------------------------------------
# Abordagem Esperada - Divisão Otimizada por Tentativa
#------------------------------------------------------------------------------------------------
# * O métod* primeiro remove todos os fatores de 2 e 3 para simplificar o número.
# * Após eliminar esses menores primos, a fatoração adicional segue uma abordagem estruturada.
# * Em vez de verificar todos os números ímpares, apenas os números da forma 6k ± 1 são testados.
# * Isso funciona porque todos os números primos maiores que 3 seguem esse padrão.
# * Ao pular verificações desnecessárias, a abordagem reduz iterações enquanto encontra
# eficientemente o maior fator primo.
def expected_approach(n: int) -> int:
    """
    Abordagem Esperada - Tempo O(sqrt(n)), Espaço O(1)
    """
    largestPrime = -1
    while n % 2 == 0:
        largestPrime = 2
        n //= 2

    while n % 3 == 0:
        largestPrime = 3
        n //= 3

    i = 5
    while i * i <= n:
        while n % i == 0:
            largestPrime = i
            n //= i

        while n % (i + 2) == 0:
            largestPrime = i + 2
            n //= (i + 2)

        i += 6

    if n > 4:
        largestPrime = n

    return largestPrime


if __name__ == "__main__":
    print("Maior Fator Primo")
    n = 100
    print("Abordagem Simples:", naive_approach(n))
    print("Abordagem Esperada:", expected_approach(n))
