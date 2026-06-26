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
            colecao,
            artigo["id"],
            artigo["titulo"],
            artigo["autores"],
            artigo["ano"],
            artigo["palavras-chave"],
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
                encontrados = encontrados.intersection(colecao.palavra_artigos[palavra])

        resultado = resultado.union(encontrados)
    return resultado


def inserir_artigo(colecao, id_artigo, titulo, autores, ano, palavras, referencias):
   
    if id_artigo in colecao.artigos:
        return False
    
    definir_artigo(
        colecao,
        id_artigo,
        titulo,
        autores,
        ano,
        palavras,
        referencias
    )
    return True


def remover_artigo(colecao, id_artigo):
    if id_artigo not in colecao.artigos:
        return False
    
    remover_indices(colecao, id_artigo)

    return True



def alterar_palavras(colecao, id_artigo, palavras_novas):
    if id_artigo not in colecao.artigos:
        return False
    
    artigo = colecao.artigos[id_artigo]

    for palavra in artigo["palavras"]:
        colecao.palavras_artigos[palavra].discard(id_artigo)

    palavra = normalizar_palavra(palavras_novas)
    artigo["palavras"] = palavra

    for palavra in palavra:
        colecao.palavras_artigos[palavra].add(id_artigo)
    return True

def alterar_referencias(colecao, id_artigo, referencias_novas):
    if id_artigo not in colecao.artigos:
        return False
    
    artigo = colecao.artigos[id_artigo]

    for referencia in artigo["referencias"]:
        colecao.citacoes[referencia].discard(id_artigo)

    referencias =  normalizar_referencias(referencias_novas)

    artigo["referencias"] = referencias

    for referencia in referencias:
        colecao.citacoes[referencia].add(id_artigo)
    
    return True


def gravar_arquivo(colecao, nome_arquivo):
    # FIXME: prepare uma lista de arquivos no formato do arquivo JSON
    lista_artigos = []
    
    for id_artigo in colecao.artigos:
        artigo = colecao.artigos[id_artigo]

        dados = {
            "id": id_artigo,
            "titulo": artigo["titulo"],
            "autores": artigo["autores"],
            "ano": artigo["ano"],
            "palavras-chave": artigo["palavras"],
            "referencias": artigo["referencias"],
        }
        lista_artigos.append(dados)


    with open(nome_arquivo, "w") as arquivo:
        json.dump(lista_artigos, arquivo, indent=2, ensure_ascii=False)
