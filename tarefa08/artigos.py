"""
FIXME: Descreva AQUI sucinta e objetivamente como você irá representar a coleção
de artigos. Reveja as instruções no enunciado da tarefa. Todos os dados da
coleção de artigos são passados para as funções por meio de um único parâmetro
colecao. Se sua coleção precisar guardar tipos distintos de dados, então você
pode utilizar um objeto do tipo SimpleNamespace, como no exemplo abaixo.
"""

import json
from collections import defaultdict
from types import SimpleNamespace


def criar_colecao():
    colecao = SimpleNamespace()
    colecao.artigos = {}
    colecao.citacoes = defaultdict(list)
    colecao.palavras_artigos = defaultdict(set)
    colecao.aut_contagem = {}
    return colecao


def obter_nome_artigo(colecao, id_artigo):
    pass


def carregar_arquivo(colecao, nome_arquivo):
    with open(nome_arquivo) as arquivo:
        lista_artigos = json.load(arquivo)

    # FIXME: carregue a lista de artigos lidos na sua coleção
    ...


def obter_numero_artigos(colecao):
    pass


def obter_palavras(colecao):
    pass


def obter_principais_autores(colecao):
    pass


def obter_referencias_orfas(colecao):
    pass


def buscar_citacoes(colecao, id_artigo):
    pass


def buscar_palavras(colecao, consulta):
    pass


def inserir_artigo(colecao, id_artigo, titulo, autores, ano, palavras, referencias):
    pass


def remover_artigo(colecao, id_artigo):
    pass


def alterar_palavras(colecao, id_artigo, palavras_novas):
    pass


def alterar_referencias(colecao, id_artigo, referencias_novas):
    pass


def gravar_arquivo(colecao, nome_arquivo):
    # FIXME: prepare uma lista de arquivos no formato do arquivo JSON
    lista_artigos = ...
    ...

    with open(nome_arquivo, "w") as arquivo:
        json.dump(lista_artigos, arquivo, indent=2, ensure_ascii=False)
