# Dado um número n, Verifique se é impar ou par.
# Retorne verdadeiro para par e falso para impar.

def naive_approach(n: int) -> bool:
    return n % 2 == 0

def expected_approach(n: int) -> bool:
    return n & 1 == 0

if __name__ == "__main__":
    print("Verificar se é Par ou Impar")
    # lista de número para testar as funções
    test_list = range(0, 10)

    print("\nAbordagem Simples |", "Abordagem Esperada")
    for i in test_list:
        print(f"{i} is ", "Par         |" if naive_approach(i) else "Impar       |",
              f"{i} is ", "Par" if expected_approach(i) else "Impar")

    # Ambas as Abordagens - Tempo O(1), Espaço (1)
