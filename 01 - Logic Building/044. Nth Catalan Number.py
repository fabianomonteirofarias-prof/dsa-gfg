#---------------------------------------------------------------------------------
# Enésimo Número Catalão
#---------------------------------------------------------------------------------
# Números catalães são definidos como uma sequência matemática composta por
# inteiros positivos, que podem ser usados para encontrar o número de possibilidades
# de várias combinações. O n-ésimo termo na sequência denotada por Cn é encontrado
# na seguinte fórmula:
#
# Os primeiros números catalães para n = 0, 1, 2, 3, 4, 5... são: 1, 1, 2, 5, 14,
# 42, 132, 429, 1430, 4862,... E assim por diante.
#
# Os números catalães aparecem em muitos problemas interessantes de contagem, como
# os seguintes.
# Conte o número de expressões contendo n pares de parênteses que estão
# corretamente correspondidos. Conte o número de possíveis Árvores de Busca Binárias
# com n chaves.
# Conte o número de árvores binárias completas (uma árvore binária enraizada é cheia
# se cada vértice tiver dois filhos ou nenhum filho) com n+1 folhas.
# Dado um número n, retorne o número de maneiras de desenhar n acordes em um círculo
# com 2 x n pontos de modo que nenhum acorde 2 se cruze. Consulte isso para mais
# aplicações.

#---------------------------------------------------------------------------------
# Abordagem Simples - Usando Recursão
#---------------------------------------------------------------------------------
# Formula:
# * C_0 = C_1 = 1
# * C_n = ∑_(i=0, n−1) C_i * C_n−i−1, para n≥2
def naive_approach(n: int) -> int:
    """
    Abordagem Simples - Tempo O(2^n)m Espaço O(n)
    """
    if n <= 1:
        return 1

    res = 0
    for i in range(n):
        res += naive_approach(i) * naive_approach(n - i - 1)

    return res

#---------------------------------------------------------------------------------
# Abordagem Esperada - Usando Recursão
#---------------------------------------------------------------------------------
# * Crie um array catalan[] para armazenar o i-ésimo número de Catalan.
# * Inicialize, catalan[0] e catalan[1] = 1.
# * Faça um loop de i = 2 até o número de Catalan dado n:
#       * Faça um loop de j = 0 até j < i e continue somando o valor de
#       catalan[j] * catalan[i - j - 1] em catalan[i].
# * Finalmente, retorne catalan[n].
def expected_approach(n: int) -> int:
    """
    Abordagem Esperada - Tempo O(n^2), Espaço(n)
    """
    # cria um array
    arr = [0] * (n + 1)
    # inicializa os primeiros números
    arr[0] = arr[1] = 1
    # loop
    for i in range(2, n+1):
        for j in range(i):
            arr[i] += arr[j] * arr[i - j - 1]

    return arr[n]

#---------------------------------------------------------------------------------
# Abordagem Alternativa Esperada - Usando o Coeficiente Binomial
#---------------------------------------------------------------------------------
def binomialCoeff(n: int, k: int) -> int:
    res = 1

    if k > n - k:
        k = n - k

    for i in range(k):
        res *= (n - i)
        res //= (i + 1)

    return res

def alternative_approach(n: int) -> int:
    """
    Abordagem Alternativa - Tempo O(n), Espaço O(1)
    """
    c = binomialCoeff(2 * n, n)
    return c // (n + 1)

#---------------------------------------------------------------------------------
# Abordagem Alternativa Esperada Otimizada- Usando o Coeficiente Binomial
#---------------------------------------------------------------------------------
# C_n = C_(n-1) * ((4n-2)/(n+1))
def optimized_approach(n: int) -> int:
    """
    Abordagem Esperada Alternativa Otimizada - Tempo O(n), Espaço O(1)
    """
    res = 1

    for i in range(2, n + 1):
        res = (res * (4 * i - 2)) // (i + 1)

    return res


if __name__ == "__main__":
    print("Enésimo Número Catalão")
    n = 10
    for i in range(1, n):
        print("----------------------------------------------")
        print("Abordagem Simples:", naive_approach(i))
        print("Abordagem Esperada:", expected_approach(i))
        print("Abordagem Alternativa:", alternative_approach(i))
        print("Abordagem Alternativa Otimizada:", optimized_approach(i))
