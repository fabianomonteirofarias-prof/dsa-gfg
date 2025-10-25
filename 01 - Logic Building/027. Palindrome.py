# Dado um inteiro n, determine se ele é um palíndromo ou não.
# Um número é chamado de palíndromo se lido de trás para frente
# continua o mesmo.

def naive_approach(n: int) -> bool:
    reverse = 0
    aux = n

    while aux:
        reverse *= 10
        reverse += aux % 10
        aux //= 10

    return reverse == abs(n)

def alternative_approach(n: int) -> bool:
    s = str(abs(n))
    length = len(s)

    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False

    return True

if __name__ == "__main__":
    print("Palíndromo")
    n = 12321
    print("Abordagem Simples:", naive_approach(n))
    print("Abordagem Alternativa:", alternative_approach(n))

    # Abordagem Simples: Tempo(d), Espaço(1)
    # Abordagem Alternativa: Tempo(d), Espaço(d)
    # d ≈ log₁₀(n)
