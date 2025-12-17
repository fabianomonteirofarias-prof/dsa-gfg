#-------------------------------------------------------------------------------
# Próxima Permutação
#-------------------------------------------------------------------------------
# Dado um array de inteiros arr[] representando uma permutação (ou seja, todos
# os elementos são únicos e dispostos em alguma ordem), encontre a próxima
# permutação lexicograficamente maior rearranjando os elementos do array. Se
# tal permutação não existir (ou seja, o array for a última permutação
# possível), rearranjar os elementos para formar a ordem mais baixa possível
# (ou seja, ordenados em ordem crescente);

#-------------------------------------------------------------------------------
# Abordagem Simples - Gerar todas permutações
#-------------------------------------------------------------------------------
def generatepermutations(res, arr, idx):
    if idx == len(arr) - 1:
        res.append(arr[:])
        return

    for i in range(idx, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]

        generatepermutations(res, arr, idx+1)

        arr[idx], arr[i] = arr[i], arr[idx]

def naive_approach(arr: list) -> list:
    """
    Abordagem Simples - Tempo O(n!), Esáço O(n)
    """
    res = []
    generatepermutations(res, arr, 0)
    res.sort()
    aux = []

    for i in range(len(res)):
        if res[i] == arr:
            if i < len(res) - 1:
                aux[:] = res[i+1]

            else:
                aux[:] = res[0]

            break

    return aux

#-------------------------------------------------------------------------------
# Abordagem Esperada - Gerar apenas a próxima permutação
#-------------------------------------------------------------------------------
def expect_approach(arr: list) -> list:
    """
    Abordagem Esperada - Tempo O(n), Espaço O(1)
    """
    n = len(arr)
    pivot = -1
    aux = arr.copy()

    for i in range(n-2, -1, -1):
        if aux[i] < aux[i+1]:
            pivot = i
            break

    if pivot == -1:
        return aux[::-1]

    for i in range(n-1, pivot, -1):
        if aux[i] > aux[pivot]:
            aux[i], aux[pivot] = aux[pivot], aux[i]
            break

    left, right = pivot + 1, n - 1
    while left < right:
        aux[left], aux[right] = aux[right], aux[left]
        left += 1
        right -=1

    return aux


if __name__ == "__main__":
    print("Próxima Permutação")
    arr = [1, 2, 3, 4, 5]
    print("Abordagem Simples:", naive_approach(arr))
    print("Abordagem Esperada:", expect_approach(arr))
