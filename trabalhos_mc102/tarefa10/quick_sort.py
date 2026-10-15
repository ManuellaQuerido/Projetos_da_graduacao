def particionar(lista, esq, dir):

    pivo = lista[esq]
    i = esq + 1
    j = dir

    while i <= j:
        while i <= j and lista[i] < pivo:
            i += 1
        while i <= j and lista[j] >= pivo:
            j -= 1
        if i < j:
            lista[i], lista[j] = lista[j], lista[i]

    lista[esq], lista[j] = lista[j], lista[esq]
    return j


def quick_sort_rec(lista, esq, dir):

    if esq >= dir:
        return

    pos_pivo = particionar(lista, esq, dir)

    quick_sort_rec(lista, esq, pos_pivo - 1)
    quick_sort_rec(lista, pos_pivo + 1, dir)


def quick_sort(lista):

    if len(lista) > 0:
        quick_sort_rec(lista, 0, len(lista) - 1)
    return lista


def main():

    numeros = list(map(int, input().split()))

    quick_sort(numeros)

    for i in range(len(numeros)):
        if i == len(numeros) - 1:
            print(numeros[i])
        else:
            print(numeros[i], end=" ")


main()