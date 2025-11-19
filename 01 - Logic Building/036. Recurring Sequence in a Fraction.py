# Dado uma fração, encontre a sequência recorrente de dígitos
# se ele existir, se não, print "No recurring sequence".

def naive_approach(a: int, b: int):
    res = ""
    mp = {}
    rem = a % b
    while (rem != 0) and (rem not in mp):
        mp[rem] = len(res)

        rem *= 10
        res += str(rem // b)
        rem %= b

    if rem == 0:
        return "No recurring sequence."

    return res[mp[rem]:]


if __name__ == "__main__":
    print("Sequência Recorrente em uma Fração")
    a, b, = 50, 2
    print("Abordagem Simples:", naive_approach(a, b))
