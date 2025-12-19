#-------------------------------------------------------------------
# Super Primo
#-------------------------------------------------------------------
# Dado um inteiro positivo n e uma tarefa de exibir todos os
# super primos menor ou igual a n.
#
# Números super primos  (também conhecidos como primos de ordem
# maior) são subsequências das sequências de números primos que
# ocupam uma posição de numeração primo como a sequência de todos
# os números primos. Os super primos são: 3, 5, 11, 17...


#-------------------------------------------------------------------
# Abordagem Simples - Usando Sieve of Eratosthenes
#-------------------------------------------------------------------
def sieve_of_eratosthenes(n: int) -> list[bool]:
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False

    return is_prime


def naive_approach(n: int) -> list[int]:
    """
    Abordagem Simples - Tempo O(n*log(log(n))), Espaço O(n)
    """
    is_prime = sieve_of_eratosthenes(n)
    prime = [i for i in range(n+1) if is_prime[i]]

    ans = []
    for i in range(len(prime)):
        if i + 1 < len(is_prime) and is_prime[i+1]:
            ans.append(prime[i])

    return ans

if __name__ == "__main__":
    print("Super Prime")
    n = 100
    print("Abordagem Simples:", naive_approach(n))
