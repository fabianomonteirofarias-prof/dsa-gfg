#-----------------------------------------------------------------------
# Torre de Hanoi
#-----------------------------------------------------------------------
# Torre de Hanói é um quebra-cabeça matemático onde temos três hastes
# (A, B e C) e N discos. Inicialmente, todos os discos são empilhados
# em valor decrescente de diâmetro, ou seja, o menor disco é colocado
# no topo e eles estão na haste A. O objetivo do quebra-cabeça é mover
# toda a pilha para outra haste (aqui considerada C), obedecendo às
# seguintes regras simples:
#   * Apenas um disco pode ser movido por vez.
#   * Cada movimento consiste em pegar o disco superior de uma das
#   pilhas e colocá-lo sobre outra pilha, ou seja, um disco só pode
#   ser movido se for o disco mais alto de uma pilha.
#   * Nenhum disco pode ser colocado sobre um disco menor.


#-----------------------------------------------------------------------
# Abordagem Simples - Usando Recursão
#-----------------------------------------------------------------------
def naive_approach(n: int, from_rod: str, to_rod: str, aux_rod: str):
    """
    Abordagem Simples - Tempo O(2^N), Espaço O(n)
    """
    if n == 0:
        return

    naive_approach(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    naive_approach(n-1, aux_rod, to_rod, from_rod)


if __name__ == "__main__":
    print("Torre de Hanoi")
    n = 3
    print("Abordagem Simples:", naive_approach(n, "A", "B", "C"))
