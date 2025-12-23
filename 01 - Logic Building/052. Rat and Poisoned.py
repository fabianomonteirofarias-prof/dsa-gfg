#-------------------------------------------------------
# Rat and Poisoned
#------------------------------------------------------
# Dado N número de garrafas em que uma delas está
# envenenada. Então, a tarefa é descobrir o número
# mínimo de ratos necessários para identificar a
# garrafa envenenada. Um rato pode beber qualquer
# número de garrafas ao mesmo tempo e, se alguma das
# garrafas tomadas for venenosa, o rato morre e não
# pode mais beber.

import math


#-------------------------------------------------------
# Abordagem Simples
#------------------------------------------------------
def naive_approach(n: int):
    """
    Abordagem Simples - Tempo O(1), Espaço O(1)
    """
    return math.ceil(math.log(n))

if __name__ == "__main__":
    print("Rat and Poisoned")
    n = 100
    print("Abordagem Simples:", naive_approach(n))