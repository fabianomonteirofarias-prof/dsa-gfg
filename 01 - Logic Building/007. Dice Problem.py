# Você recebe um dado cúbico (6 faces). Todos as faces possuem
# um número diferente, entre 1 e 6 (semelhante a dado normal).
# Você vai receber uma face desse cubo, sua tarefa é adivinhar
# qual é o número oposto a face do cubo.

def naive_approach(n: int) -> int:
    if n == 1: return 6
    elif n == 2: return 5
    elif n == 3: return 4
    elif n == 4: return 3
    elif n == 5: return 2
    else: return 1

def alternative_approach_list(n: int) -> int:
    opposite_face: list = [6, 5, 4, 3, 2, 1]
    return opposite_face[n-1]

def alternative_approach_dict(n: int) -> int:
    opposite_face: dict = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    return opposite_face[n]

def expected_approach(n: int) -> int:
    return 7 - n

if __name__ == "__main__":
    print("Problema do Dado\n")

    # lista para teste
    test_list = range(1, 7)

    print("Abordagens")
    print("Simples", "|", "Alternativa (list)", "|", "Alternativa (dict)", "|", "Esperado")
    for i in test_list:
        print(naive_approach(i), "|",
              alternative_approach_list(i), "|",
              alternative_approach_dict(i), "|",
              expected_approach(i))


    # Ambas Abordagens - Tempo(1), Espaço(1)
