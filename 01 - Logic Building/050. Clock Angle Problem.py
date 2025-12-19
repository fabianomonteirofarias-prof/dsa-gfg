#--------------------------------------------------------------
# Clock Angle Problem
#--------------------------------------------------------------
# Dado uma string s representando o tempo de 24 horas no formato
# ("HH:MM"), determine o menor ângulo entre a hora e os minutos
# presente no relógio analógico (em graus).

#--------------------------------------------------------------
# Abordagem Simples - Usando a Formula
#--------------------------------------------------------------
def naive_approach(s: str) -> float:
    """
    Abordagem Simples - Tempo O(1), Espaço O(1)
    """
    # pega as horas e os minutos
    hour, minutes = s.split(":")
    h, m = int(hour), int(minutes)

    # calcula os valores dos ângulos de cada um
    ang_h = 0.5 * ((h % 12) * 60 + m) # cada minuto de hora equivale a 0.5 gruas
    ang_m = 6 * m         # cada minuto equivale a 6 graus

    # calcula a diferença entre os ângulos
    angle = abs(ang_h - ang_m)

    # retorna o menor ângulso
    return min(360 - angle, angle)

if __name__ == "__main__":
    print("Problema do Ângulo do Relógio")
    s = "21:45"
    print("Abordagem Simples:", naive_approach(s))
