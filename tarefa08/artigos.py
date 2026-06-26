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
    colecao.citacoes = defaultdict(set)
    colecao.palavras_artigos = defaultdict(set)
    colecao.aut_contagem = defaultdict(int)

    return colecao


def obter_nome_artigo(colecao, id_artigo):
    if id_artigo in colecao.artigos:
        return colecao.artigos[id_artigo]["titulo"]
    
    return None


def normalizar_palavra(palavra):
    lista = []

    for palavra in palavra:
        if palavra != "" and palavra not in lista:
            lista.append(palavra)
    
    lista.sort()

    return lista
    

def carregar_arquivo(colecao, nome_arquivo):
    with open(nome_arquivo) as arquivo:
        lista_artigos = json.load(arquivo)
    
    # FIXME: carregue a lista de artigos lidos na sua coleção
    
    for artigo in lista_artigos:

        definir_artigo(
            artigo["id"],
            artigo["titulo"],
            artigo["autores"],
            artigo["ano"],
            artigo["palavras"],
            artigo["referencias"],
        )


def obter_numero_artigos(colecao):

    return len(colecao.artigos)


def obter_palavras(colecao):
    palavras = []

    for palavras in colecao.palavras_artigos:
        if len(colecao.palavras_artigos[palavras]) > 0:
            palavras.append(palavras)
    
    palavras.sort()

    return palavras


def obter_principais_autores(colecao):
    if len(colecao.aut_contagem) == 0:
        return 0, []
    
    maior = max(colecao.aut_contagem.values())

    autores = []
    for autor in colecao.aut_contagem:
        if colecao.aut_contagem[autor] == maior:
            autores.append(autor)

    autores.sort()
    
    return maior, autores


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
