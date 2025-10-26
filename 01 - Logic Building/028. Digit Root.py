# The digital root of a positive integer is found by summing the digits of
# the integer. If the resulting value is a single digit then that digit is
# the digital root. If the resulting value contains two or more digits,
# those digits are summed and the process is repeated. This is continued as
# long as necessary to obtain a single digit.
#
# Given a number, the task is to find its digital root. The input number may
# be large and it may not be possible to store even if we use long long int.

def naive_approach(n: int) -> int:
    s = str(n)
    while len(s) != 1:
        n = 0
        for d in s:
            n += int(d)
        s = str(n)
    return n

def expected_approach(n: int) -> int:
    if n == 0:
        return 0

    if n % 9 == 0:
        return 9
    return n % 9

if __name__ == "__main__":
    print("Digit Root")
    # n = 1234
    n = 5674
    print("Abordagem Simples:", naive_approach(n))
    print("Abordagem Esperado:", expected_approach(n))

    # Abordagem Simples: Tempo(d), Espaço(d)
    # Abordagem Esperada: Tempo(1), Espaço(1)
    # d = log_₁₀(n)