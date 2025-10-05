# Dado dois números a e b, a tarefa é trocar eles.

def naive_approach(a: int, b: int) -> (int, int):
    aux = a
    a = b
    b = aux
    return a, b

def expected_approach(a: int, b:int) -> (int, int):
    # a, b = b, a
    return b, a

if __name__ == "__main__":
    print("Trocando Dois Números\n")

    # Números para teste
    a, b = 10, 20
    print("a:", a, "b:", b)
    print("Abordagem Simples: ", naive_approach(a, b))
    print("Abordagem Esperada: ", expected_approach(a, b))

    # Ambas Abordagens - Tempo(1), Espaço(1)
