"""
A coleção é representada por um objeto SimpleNamespace com quatro atributos:

- artigos: guarda os dados de cada artigo.
- citacoes: guarda quais artigos citam cada referência.
- palavra_artigos: guarda os artigos de cada palavra-chave.
- autor_contagem: guarda a quantidade de artigos de cada autor.

"""

import json
from collections import defaultdict
from types import SimpleNamespace


def criar_colecao():

    colecao = SimpleNamespace()

    colecao.artigos = {}
    colecao.citacoes = defaultdict(set)
    colecao.palavra_artigos = defaultdict(set)
    colecao.autor_contagem = {}

    return colecao


def obter_nome_artigo(colecao, id_artigo):

    if id_artigo in colecao.artigos:
        return colecao.artigos[id_artigo]["titulo"]

    return None


def normalizar_palavras(palavras):

    lista = []

    for palavra in palavras:
        if palavra != "" and palavra not in lista:
            lista.append(palavra)

    lista.sort()

    return lista


def normalizar_referencias(referencias):

    lista = []

    for referencia in referencias:
        if referencia not in lista:
            lista.append(referencia)

    lista.sort()

    return lista


def remover_indices(colecao, id_artigo):

    artigo = colecao.artigos[id_artigo]

    for autor in set(artigo["autores"]):

        colecao.autor_contagem[autor] -= 1

        if colecao.autor_contagem[autor] == 0:
            del colecao.autor_contagem[autor]

    for palavra in artigo["palavras"]:
        colecao.palavra_artigos[palavra].discard(id_artigo)

    for referencia in artigo["referencias"]:
        colecao.citacoes[referencia].discard(id_artigo)