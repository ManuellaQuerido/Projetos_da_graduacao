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
                            