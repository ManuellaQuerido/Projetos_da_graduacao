"""FIXME: Descreva AQUI sucinta e objetivamente como você irá representar a coleção
de artigos. Reveja as instruções no enunciado da tarefa. Todos os dados da
coleção de artigos são passados para as funções por meio de um único parâmetro
colecao. Se sua coleção precisar guardar tipos distintos de dados, então você
pode utilizar um objeto do tipo SimpleNamespace, como no exemplo abaixo.
"""
 
import json
from types import SimpleNamespace
 
 
def criar_colecao():

    colecao = SimpleNamespace()

    colecao.id_a = [] # id_artigo
    colecao.ano = []
    colecao.ref = [] # referencias
    colecao.p = [] # palavras
    colecao.aut = [] # autores
    colecao.tit = [] # títulos

    return colecao
 
 
def obter_nome_artigo(colecao, id_artigo):

    if id_artigo in colecao.id_a:
        posicao = colecao.id_a.index(id_artigo)
        return colecao.tit[posicao]
    
    return None
 
 
def carregar_arquivo(colecao, nome_arquivo):
    with open(nome_arquivo) as arquivo:
        lista_artigos = json.load(arquivo)
        
        for artigo in lista_artigos:
            colecao.id_a.append(artigo["id"])
            colecao.ano.append(artigo["ano"])
            colecao.ref.append(artigo["referencias"])
            colecao.p.append(artigo["palavras-chave"])
            colecao.aut.append(artigo["autores"])
            colecao.tit.append(artigo["titulo"])
 
def obter_numero_artigos(colecao):
    return len(colecao.id_a)
 
 
def obter_palavras(colecao):
    palavras = []

    for lista in colecao.p:
        for palavra in lista:
            if palavra not in palavras:
                palavras.append(palavra)
    
    palavras.sort()

    return palavras
 

def obter_principais_autores(colecao):
    contagem = {}

    for lista in colecao.aut:
        for autor in lista:
            if autor not in contagem:
                contagem[autor] = 1
            else:
                contagem[autor] += 1
    
    if len(contagem) == 0:
        return 0, []
    maior = max(contagem.values())

    principais = []

    for autor in contagem:
        if contagem[autor] == maior:
            principais.append(autor)

    principais.sort()
    return maior, principais
 
 
def obter_referencias_orfas(colecao):
    referencias = []

    for lista in colecao.ref:
        for referencia in lista:
            if referencia not in colecao.id_a:
                if referencia not in referencias:
                    referencias.append(referencia)
    
    referencias.sort()
    return referencias

 
def buscar_citacoes(colecao, id_artigo):
    citacoes = set()

    for i in range(len(colecao.id_a)):
        if id_artigo in colecao.ref[i]:
            citacoes.add(colecao.id_a[i])
    
    return citacoes
 
 
def buscar_palavras(colecao, consulta):
    palavras = set()

    for i in range(len(colecao.id_a)):
        for grupo in consulta:
            encontrou = True
            
            for palavra in grupo:
                if palavra not in colecao.p[i]:
                    encontrou = False
                    break
            
            if encontrou:
                palavras.add(colecao.id_a[i])
    
    return palavras
 
 
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
 