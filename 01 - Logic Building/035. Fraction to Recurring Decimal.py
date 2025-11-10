# Dado dois inteiros a e b (b != 0), a tarefa é retornar a fração a/b no
# formato de string. Se a parte fracionária estiver repetindo, coloque a parte
# repetitiva em parênteses.

def naive_approach(a: int, b:int) -> str:
    # signal (+/-)
    aux = "-" if (a < 0) ^ (b < 0) else ""
    # turn absolute value
    a, b = abs(a), abs(b)
    # first part
    aux += str(a // b)
    rem = a % b # rest of division

    if rem == 0: # if not rest, return answer
        return aux

    # point
    aux += "."
    mp = {}

    while rem > 0:
        if rem in mp:
            aux = aux[:mp[rem]] + "(" + aux[mp[rem]:] + ")"
            break

        mp[rem] = len(aux)
        rem *= 10

        aux += str(rem // b)
        rem %= b

    return aux



if __name__ == "__main__":
    print("Fração para Decimal Recorrente")
    # a, b = 2/9 # 0.(2)
    # a, b = 21, 99 # 0.(21)
    # a, b = 213, 999 # 0.(213)
    # a, b = 2134, 9999 # 0.(2134)
    a, b = 21345, 99999 # 0.(21345)
    print("Abordagem Simples:", naive_approach(a, b))

    # Abordagem Simples - Tempo O(max(log_10(a), log_10(b))), Espaço O(max(log_10(a), log_10(a)))
