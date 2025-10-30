# Dado um número, a tarefa é verificar se o número é divisível por
# 4 ou não. O número de entrada pode ser grande e pode não ser
# possível armazenar mesmo se usarmos long long int.

def naive_approach(n: int) -> bool:
    return n % 4 == 0

def alternative_approach(n: int) -> bool:
    s = str(n) # number to string
    l = len(s) # number order

    if l == 0:
        return False

    elif l == 1:
        return int(s[l-1]) % 4 == 0

    # else
    return int(s[-2:]) % 4 == 0


if __name__ == "__main__":
    print("Divisível por 4")
    # n = 1124
    # n = 1234567589333862
    n = 363588395960667043875487
    print("Abordagem Simples:", naive_approach(n))
    print("Abordagem Alternativa:", alternative_approach(n))

    # Abordagem Simples - Tempo(1), Espaço(1)
    # Abordagem Alternativa - Tempo(1), Espaço(1)
