# Dado um número em forma de string s, Verifique se o número
# é divisível por 11 ou não. O número inserido deve ser grande
# e ele não deve ser possível de armazenar até mesmo se usarmos
# long long int.


def naive_approach(s: str) -> bool:
    return int(s) % 11 == 0

def expected_approach(s: str) -> bool:
    sum_dig_even = 0
    sum_dig_odd = 0

    for i in range(len(s)):
        dig = int(s[i])

        if i % 2 == 0:
            sum_dig_even += dig
        else:
            sum_dig_odd += dig

    return (sum_dig_odd - sum_dig_even) % 11 == 0


if __name__ == "__main__":
    print("Divisibilidade por 11")
    # s = "11"
    # s = "76945"
    # s = "7695"
    s = "1234567589333892"
    print("Abordagem simples:", naive_approach(s))
    print("Abordagem Esperada:", expected_apprach(s))

    # n = length of string
    # Abordagem Simples - Tempo O(n), Espaço O(1)
    # Abordagem Esperada - Tempo O(n), Espaço O(1)