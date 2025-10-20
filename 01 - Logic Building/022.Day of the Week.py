# Dado uma data (dia, mês e ano), a tarefa é determinar o dia da semana
# na qual a data cai. A função deve ser capaz de calcular o dia de qualquer
# data do passado ou do futuro. A função deve retornar valores de 0 a 6, onde
# 0 significa Domingo, 1 segunda e por aí vai.

def expected_approach(day: int, month: int, year: int) -> int:
    month_code = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    return (year + int(year / 4) - int(year / 100) + int(year / 400) + month_code[month - 1] + day)%7

if __name__ == "__main__":
    print("Dia da Semana")
    # day, month, year = 15, 6, 1995
    # day, month, year = 30, 8, 2010
    day, month, year = 29, 2, 2016
    print("Abordagem Esperada:", expected_approach(day, month, year))

    # Abordagem Esperada - Tempo(1), Espaço(1)
