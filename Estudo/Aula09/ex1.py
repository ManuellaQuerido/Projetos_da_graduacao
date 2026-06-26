nome = input()
if nome == nome:
    print(f' {nome} que nome lindo!')
else:
    print(f'{nome}, bom dia!')


def obter_numero_artigos(colecao):

    return len(colecao.artigos)


def obter_palavras(colecao):

    palavras = []

    for palavra in colecao.palavra_artigos:

        if len(colecao.palavra_artigos[palavra]) > 0:
            palavras.append(palavra)

    palavras.sort()

    return palavras


def obter_principais_autores(colecao):

    if len(colecao.autor_contagem) == 0:
        return 0, []

    maior = max(colecao.autor_contagem.values())

    autores = []

    for autor in colecao.autor_contagem:

        if colecao.autor_contagem[autor] == maior:
            autores.append(autor)

    autores.sort()

    return maior, autores


def obter_referencias_orfas(colecao):

    referencias = []

    for referencia in colecao.citacoes:

        if len(colecao.citacoes[referencia]) > 0:

            if referencia not in colecao.artigos:
                referencias.append(referencia)

    referencias.sort()

    return referencias


def buscar_citacoes(colecao, id_artigo):

    if id_artigo in colecao.citacoes:
        return colecao.citacoes[id_artigo]

    return set()


def buscar_palavras(colecao, consulta):

    resultado = set()

    for grupo in consulta:

        primeiro = True
        encontrados = set()

        for palavra in grupo:

            if palavra not in colecao.palavra_artigos:
                encontrados = set()
                break

            if primeiro:
                encontrados = set(colecao.palavra_artigos[palavra])
                primeiro = False
            else:
                encontrados = encontrados.intersection(
                    colecao.palavra_artigos[palavra]
                )

        resultado = resultado.union(encontrados)

    return resultado