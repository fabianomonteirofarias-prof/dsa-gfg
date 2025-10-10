# Dado dois retângulos, descubra se dois retângulos se sobrepõe ou não.
# Note que um retângulo pode ser representado por duas coordenadas,
# superior esquerda e inferior direito. Então, principalmente, recebemos
# as quatro seguintes coordenadas:

# l1: Superior Esquerda coordenada do primeiro retângulo.
# r1: Inferior Direito coordenada do primeiro retângulo.
# l2: Superior Esquerdo coordenada do segundo retângulo.
# r2: Inferior Direito coordenada do segundo retângulo.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def approach(l1, r1, l2, r2) -> bool:
    if l2.x > r1.x or r2.x < l1.x:
        return False
    if l2.y < r1.y or r2.y > l1.y:
        return False

    return True

if __name__ == "__main__":
    print("Retângulos Sobrepostos")
    l1, r1 = Point(0, 10), Point(10, 0)
    l2, r2 = Point(-10, 5), Point(-1, 0)

    print('Abordagem:', approach(l1, r1, l2, r2))

    # Abordagem - tempo(1), Espaço(1)