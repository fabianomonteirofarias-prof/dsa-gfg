# Dado duas coordenadas (x1, y1) e (x2, y2) de uma gráfico bidimensional. Encontre a distância entre eles.

import math

def approach(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))

if __name__ == "__main__":
    print("Distância Entre Dois Números")
    x1, y1, x2, y2 = 3, 4, 7, 7
    print("Abordagem:", approach(x1, y1, x2, y2))

    # Abordagem - Tempo(1), Espaço(1)