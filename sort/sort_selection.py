def buscaMenor(arr):
    menor = arr[0]
    menor_index = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_index = i
    return menor_index


def ordenacao_selecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor_index = buscaMenor(arr)
        novo_arr.append(arr.pop(menor_index))
    return novo_arr


print(ordenacao_selecao([5, 3, 6, 2, 10]))
