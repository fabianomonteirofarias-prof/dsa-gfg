# Dado um número n, mostre sua tabela de multiplicação até 10.

def naive_approach(n: int) -> None:
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")

def alternative_approach(n: int) -> None:
    i:int = 1
    while i < 11:
        print(n, " * ", i, " = ", n * i)
        i += 1

def recursive_approach(n: int, i: int = 1) -> None:
    if i == 11:
        return

    print("%d * %d = %d" % (n, i, n * i))

    recursive_approach(n, i + 1)

if __name__ == "__main__":
    print("Tabela de Multiplicação")

    # número de teste
    n = 10

    print("\nAbordagem Simples")
    naive_approach(n)

    print("\nAbordagem Alternativa")
    alternative_approach(n)

    print("\nAbordagem Recursiva")
    recursive_approach(n)

    # Todas as Abordagens - Time O(1), Space O(1)
