# Dado um número s representado como uma string, determine
# se o inteiro representado é divisível por 13 ou não.

def naive_approach(s: str) -> bool:
    return int(s) % 13 == 0

def expected_approach(s: str) -> bool:
    # Step 1: Pad the number so its length is a multiple of 3
    if len(s) % 3 != 0:
        s += "0" * (3 - len(s) % 3)

    sum_ = 0
    i = len(s) - 1
    p = 1
    while i >= 0:
        # Step 2: Split into 3-digit blocks from right to left
        block = 0

        block += int(s[i])
        i -= 1

        block += int(s[i]) * 10
        i -= 1

        block += int(s[i]) * 100
        i -= 1

        # Step 3: Apply alternating signs starting with + on the rightmost block
        # Step 4: Sum the results
        sum_ += block * p
        p *= (-1)

    sum_ = abs(sum_)
    # Step 5: Check divisibility by 13
    return sum_ % 13 == 0

def alternative_approach(s: str) -> bool:
    rem = 0
    for ch in s:
        rem = (rem * 10 + int(ch)) % 13

    return rem == 0

if __name__ == "__main__":
    print("Divisível por 13")
    # s = "13"
    s = "2911285"
    # s = "27"
    print("Abordagem Simples:", naive_approach(s))
    print("Abordagem Esperada:", expected_approach(s))
    print("Abordagem Alternativa", alternative_approach(s))

    # n = length of s
    # Abordagem Simples - Tempo O(n), Espaço O(1)
    # Abordagem Esperada - Tempo O(n), Espaço O(1)
    # Abordagem Alternative - Tempo O(n), Espaço O(1)
