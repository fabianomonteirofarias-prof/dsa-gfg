#-------------------------------------------------------------------------------------------
# Fatorização de Primos
#-------------------------------------------------------------------------------------------
# Dado um inteiro n, encontre todos os fatores primos de n. Um fator primo é um número que
# divide n exatamente (sem deixar resto).


#-------------------------------------------------------------------------------------------
# Abordagem Simples - Fatorização Usando Divisão por Tentativa
#-------------------------------------------------------------------------------------------
# Abordagem passo a passo:
# * Comece verificando se n é divisível por 2.
#   * Se sim, armazene 2 como um fator primo único e divida n repetidamente por 2.
# * Passe por números ímpares i de 3 a √n:
#   * Se i dividir n, armazene i como um fator primo único.
#   * Continue dividindo n por i até que não seja mais divisível.
# * Após o loop, se n > 2, é um primo e deve ser armazenado.
# * Isso garante que todos os fatores primos únicos sejam capturados de forma eficiente.
# * O algoritmo evita duplicados ao remover completamente cada fator primo uma vez encontrado.
def naive_approach(n: int) -> list:
    """
    Abordagem Simples - Tempo O(sqrt(n)), Espaço O(log(n))
    """

    res = []

    # se n divisível por 2
    if n % 2 == 0:
        # armazena 2
        res.append(2)
        while n % 2 == 0:
            n //= 2

    # passa pelos números ímpares
    i = 3
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            while n % i == 0:
                n //= i

        i += 2

    # armazenar se o que sobrou for > 2
    if n > 2:
        res.append(n)

    return res


#-------------------------------------------------------------------------------------------
# Abordagem Esperada - Peneira de Eratóstenes (Menor Fator Primo)
#-------------------------------------------------------------------------------------------
# * Precalcule o SPF para tod* número até n:
#   - Crie um array spf[] de tamanho n+1, onde spf[i] armazena o menor fator primo de i.
#   - Inicialize spf[i] = i para tod* i.
#   - Use a peneira de Eratóstenes, para cada primo i, marque spf[j] = i para todos os
#   múltiplos j de i (se ainda não estiver marcado).
# * Para encontrar fatores primos únicos de um número n:
#   - Divida repetidamente n por spf[n] (ou seja, n = n/spf[n]).
#   - Armazene cada novo spf[n] encontrado em um conjunto (para mantê-lo único e em ordem
#   crescente).
#   - Continue até n se tornar 1.

import math


def smallest_prime_fator(n: int) -> list:
    """
    Retorna uma lista dos menores fatores primos dos
    index da lista de tamanho n.

    Big O Notation:
    - Tempo O(n * log(n))
    - Espaço O(n)
    """
    spf = [i for i in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i

    return spf


def prime_factors(n, spf):
    """
    Encontra apenas os fatores primos - Tempo O(log(n)), Espaço O(1).
    """
    unique_factors = set()
    while n > 1:
        unique_factors.add(spf[n])
        n //= spf[n]

    return sorted(unique_factors)


def expected_approach(n: int) -> list:
    """
    Abordagem Esperada - Tempo O(n * log(log(n))), Espaço O(n)
    """
    spf = smallest_prime_fator(n)
    return prime_factors(n, spf)


if __name__ == "__main__":
    print("Fatorização de Primos")
    # n = 100
    # n = 11
    n = 60
    print("Abordagem Simples:", naive_approach(n))
    print("Abordagem Esperada:", expected_approach(n))
