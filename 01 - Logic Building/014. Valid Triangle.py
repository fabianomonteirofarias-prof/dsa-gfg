# Dado 3 lados, verifique se o triângulo é valido ou não.

def approach(a, b, c) -> bool:
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    return True

if __name__ == "__main__":
    print("Validação de Triângulos")
    a, b, c = 1, 10, 12
    print("Abordagem:", approach(a, b, c))

    # Abordagem - Tempo(1), Espaço(1)