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