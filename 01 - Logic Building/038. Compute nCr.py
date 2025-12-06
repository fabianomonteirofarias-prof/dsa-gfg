#---------------------------------------------------------------------------------
# COMPUTE nCr
#---------------------------------------------------------------------------------
# Dados dois números n e r, a tarefa é encontrar o valor de nCr.
# Combinações representam o número de maneiras de escolher r
# elementos de um conjunto de n elementos distintos, sem considerar
# a ordem em que são selecionados. A fórmula para calcular
# combinações é:

# nCr = n! / r ! * (n - r)!

#---------------------------------------------------------------------------------
# Solução Simples
#---------------------------------------------------------------------------------
# Usando a função fatorial e a fórmula matemática. Resolve n!, r! e (n - r)!
# separadamente e depois resolve a equação. Essa abordagem é ineficiente para
# números valores grandes, causando overflow e requer cálculos excessivos.

def fatorial(n: int):
    """
    Função Fatorial - Solução Iterativa - Tempo O(n), Espaço O(1).
    Ex.:
        fatorial(5) = 5 * 4 * 3 * 2 * 1 = 120
    """
    res = 1
    # enquanto houver 'n'
    while n:
        # guardar res * n
        res *= n
        # decrementar 'n'
        n -= 1

    return res

def naive_approach(n: int, r: int) -> int:
    """
    Abordagem Simples - Fatorial e Fórmula Matemática - Tempo O(n), Espaço O(1).
        nCr = n! / r ! * (n - r)!
    """
    # sem combinações válidas se n - r for negativo
    if r > n:
        return 0

    # aplicação da fórmula de nCr
    return fatorial(n) // (fatorial(r) * fatorial(n - r))


#---------------------------------------------------------------------------------
# Solução com Recursividade
#---------------------------------------------------------------------------------
# Usando os casos bases (casos de parada):
#   - Se r > n: não existe combinações válidas.
#   - Se r igua a zero ou n: existe apenas uma combinação possível.
# Para outros valores a função calcula o valor de nCr somando o número de combinações
# possíveis ao incluir o elemento atual e o número de combinações possíveis ao não
# incluir o elemento atual.

def recursive_approach(n: int, r: int) -> int:
    """
    Abordagem Recursiva - Tempo O(2^n) e Espaço O(n).
    """
    # sem combinações válidas
    if r > n:
        return 0

    # caso de parada
    if r == 0 or r == n:
        return 1

    # inclui ou exclui o elemento atual
    return recursive_approach(n - 1, r - 1) + recursive_approach(n - 1, r)


#---------------------------------------------------------------------------------
# Solução Evitando Cálculos Fatorial
#---------------------------------------------------------------------------------
# Ao invés de calcular o fatorial por completo, reconhecemos que há termos em comum
# de r! em (n - r)! e as cancelamos.

def multiplier(start:int, end:int) -> int:
    """
    Função Auxiliar - Tempo O(end), Espaço O(1)
    Multiplicação entre os valores inteiros de um intervalo.
    """
    # não é necessário fazer nenhum calculo se forem iguais
    if start == end:
        return start

    # multiplica até chegar no end
    res = 1
    while start <= end:
        res *= start
        start += 1

    return res

def avoid_fatorial_approach(n: int, r: int) -> int:
    """
    Abordagem Sem Fatorial - Tempo O(n), Espaço O(1)
    """
    # não há combinações válidas
    if r > n:
        return 0

    # existe apenas uma combinação possível
    if r == 0 or r == n:
        return 1

    # usar max e min para reduzir o número de multiplicações
    max_val = max(r, n-r)
    min_val = min(r, n-r)

    # numerador e denominador com partes em comum "canceladas"
    nume = multiplier(max_val + 1, n)
    deno = multiplier(1, min_val)

    return nume // deno

#---------------------------------------------------------------------------------
# Solução Usando a Fórmula do Coeficiente Binomial
#---------------------------------------------------------------------------------
# Um coeficiente binomial C(n, k) pode ser definido como o coeficiente de X^k nac
# expansão de (1 + X)n. Um coeficiente binomial C(n, k) também fornece o número
# de maneiras, desconsiderando a ordem, pelas quais k objetos podem ser escolhidos
# entre n objetos; mais formalmente, o número de subconjuntos de k elementos (ou
# k-combinações) de um conjunto de n elementos.

def expected_approach(n: int, r: int) -> int:
    """
    Abordagem com Coeficiente Binomial - Tempo O(r), Espaço O(1)
    """
    sum_ = 1

    # calcula os valores de n escolhidos em r usando a formula coef. binomial
    for i in range(1, r + 1):
        sum_ = sum_ * (n - r + i) // i
    return sum_


#---------------------------------------------------------------------------------
# Solução Usando Logaritmo
#---------------------------------------------------------------------------------
# A fórmula logarítmica para nCr é uma alternativa à fórmula fatorial que evita
# calcular fatoriais diretamente e é mais eficiente para valores grandes de n e r.
# Ele usa a identidade log(n!) = log(1) + log(2) +... + log(n) para expressar o
# numerador e o denominador do nCr em termos de somas de logaritmos, o que
# permite calcular o nCr usando as operações logarítmicas. Essa abordagem é mais
# rápida e muito eficiente. A fórmula logarítmica para nCr é:
#           nCr = exp( log(n!) - log(r!) - log((n-r)!))
import math

def alternative_approach(n: int, r: int) -> int:
    """
    Abordagem com Logaritmos - Tempo O(r), Espaço O(1)
    """

    # não existem combinações válidas
    if r > n:
        return 0

    # existe apenas uma combinação possível
    if r == 0 or r == n:
        return 1

    res = 0
    for i in range(r):
        # log(n!) - log(r!) - log((n - r)!)
        res += math.log(n - i) - math.log(i + 1)

    return round(math.exp(res))


if __name__ == "__main__":
    print("Compute nCr")
    n, r = 5, 2
    print("Abordagem Simples:", naive_approach(n, r))
    print("Abordagem Recursiva:", recursive_approach(n, r))
    print("Abordagem Sem Fatorial:", avoid_fatorial_approach(n, r))
    print("Abordagem Esperada:", expected_approach(n, r))
    print("Abordagem Alternativa:", alternative_approach(n, r))

    # Abordagem Simples - Tempo O(n), Espaço O(1)
    # Abordagem Recursiva - Tempo O(2^n), Espaço O(n)
    # Abordagem Sem Fatorial - Tempo O(n), Espaço O(1)
    # Abordagem Esperada - Tempo O(r), Espaço O(1)
    # Abordagem Alternativa - Tempo O(r), Espaço O(1)