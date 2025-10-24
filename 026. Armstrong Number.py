# Given a number x, determine whether the given number is Armstrong's
# number or not. A positive integer of n digits is called an Armstrong
# number of order n (order is the number of digits) if
#
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
#
# Here a, b, c and d are digits of input number abcd.....

def order(n: int) -> int:
    count = 0
    while n:
        count += 1
        n //= 10

    return  count

def naive_approach(x: int) -> bool:
    number_order = order(x)

    res = 0 # resposta
    aux = x # auxiliar

    while aux:
        # last digit power by number of digits
        res += pow(aux%10, number_order)
        # remove the last digit from var x
        aux //= 10

    return res == x

def alternative_approach(x: int) -> bool:
    string_number = str(x)
    order_number = len(string_number)
    res = 0

    for d in string_number:
        res += pow(int(d), order_number)

    return res == x

if __name__ == "__main__":
    print("Número de Armstrong")
    # n = 153 # True
    # n = 9474 # True
    n = 123 # false

    print("Abordagem Simples:", naive_approach(n))
    print("Abordagem Alternativa:", alternative_approach(n))

    # Abordagem Simples - Tempo(n), Espaço(1)
    # Abordagem Alternativa - Tempo(n), Espaço(1)