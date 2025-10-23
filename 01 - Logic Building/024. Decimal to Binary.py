# Given a non negative number n, the task is to convert
# the given number into an equivalent binary representation.

def method_approach(n: int) -> str:
    return bin(n)[2::]

def division_approach(n: int) -> str:
    binary = []
    while n:
        bit = n % 2
        binary.append(str(bit))
        n //= 2
    binary.reverse()
    return "".join(binary)

def recursion_approach(n: int) -> str:
    def bin_to_dec(n, binary: list):
        if n == 0:
            return

        bin_to_dec(n//2, binary)

        binary.append(str(n % 2))

    #
    if n == 0:
        return "0"

    binary = []
    bin_to_dec(n, binary)

    return "".join(binary)

def bitwise_approach(n: int) -> str:
    binary = ""
    while n:
        binary += str(n & 2)
        n >>= 1
    return binary

if __name__ == "__main__":
    print("Decimal para Binário")
    n = 1000
    print("Abordagem usando Bin Método:", method_approach(n))
    print("Abordagem usando Divisão:", division_approach(n))
    print("Abordagem Recursiva:", recursion_approach(n))
    print("Abordagem Bitwise:", bitwise_approach(n))

    # Todas abordagem - Tempo(log_2(n)), Espaço(log_2(n))
