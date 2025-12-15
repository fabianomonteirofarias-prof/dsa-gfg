#----------------------------------------------------------------------------------
# Power Set
#----------------------------------------------------------------------------------
# O Conjunto Potência P(S) de um conjunto S é um conjunto de todos os subconjuntos
# de S. Por exemplo: S = {a, b, c} então P(S) = {{}, {a}, {b}, {c}, {a,b}, {a, c},
# {b, c}, {a, b, c}} Se S tem n elementos então P(s) terá 2^n elementos.

#----------------------------------------------------------------------------------
# Abordagem - Usando Representação Binária de 0 a 2^n - 1
#----------------------------------------------------------------------------------
def naive_approach(s: list) -> list:
    """
    Abordagem Simples - Tempo O(n * 2^n), Espaço O(1)
    """
    n = len(s)
    result = []
    for i in range(1 << n):
        subset = ""
        for j in range(n):
            if i & (1 << j):
                subset += s[j]

        result.append(subset)

    return result


if __name__ == "__main__":
    print("Power Set")
    s = ["a", "b", "c", "d"]
    print("Abordagem Simples:", naive_approach(s))

