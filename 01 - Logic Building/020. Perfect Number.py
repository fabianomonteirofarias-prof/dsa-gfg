# Um número é um número perfeito se for igual à soma
# de seus divisores próprios, isto é, a soma de seus
# divisores positivos excluindo o próprio número.
# Descubra se um determinado inteiro positivo n é
# perfeito ou não.


def naive_approach(n: int) -> bool:
    s = 1 # soma
    for i in range(2, n):
        if n % i == 0:
            s += i

    return s == n

def expected_approach(n: int) -> bool:
    s = 1 # soma

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            if i * i != n:
                s += i + n // i
            else:
                s += i

    return s == n

if __name__ == "__main__":
    print("Número Perfeito")

    test_list = [6, 15, 28, 496, 8128, 33_550_336]
    print("Abordagem Simples:")
    for n in test_list:
        print("n =", n, "->", naive_approach(n))

    print("Abordagem Esperada:")
    for n in test_list:
        print("Abordagem Esperada:", "n =", n, "->", expected_approach(n))

    # Abordagem Simples: Tempo(n), Espaço(1)
    # Abordagem Esperada: Tempo(sqrt(n)), Espaço(1)