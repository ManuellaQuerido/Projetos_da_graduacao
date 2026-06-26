"""
A coleção de artigos é representada por um objeto SimpleNamespace com os
seguintes atributos:

- artigos: dict que mapeia o id de cada artigo para um dicionário com os
  campos 'titulo', 'autores' (lista de autores na ordem fornecida),
  'palavras' (lista de palavras-chave em ordem lexicográfica), 'ano' e
  'referencias' (lista de ids referenciados em ordem de código). A ordem
  das chaves desse dict corresponde à ordem em que os artigos foram
  carregados/inseridos (dicionários em Python preservam a ordem de
  inserção); essa é a ordem usada para gravar o arquivo de saída.

- citacoes: dict que mapeia cada id referenciado para o conjunto (set) dos
  ids dos artigos que o referenciam (índice inverso de citações). Permite
  responder BUSCAR-CITACOES em tempo proporcional apenas ao número de
  citações encontradas, sem percorrer toda a coleção. Também é usada para
  calcular as referências órfãs: são os ids que aparecem como chave em
  'citacoes' (logo, são citados por algum artigo), mas que não aparecem
  em 'artigos'.

- palavra_artigos: dict que mapeia cada palavra-chave para o conjunto dos
  ids dos artigos que a possuem (índice de palavras-chave). Permite
  implementar BUSCAR-PALAVRAS com interseções (operador E) e uniões
  (operador OU) de conjuntos, sem repetir a busca por uma mesma palavra
  dentro de uma mesma consulta.

- autor_contagem: dict que mapeia cada autor para o número de artigos da
  coleção em que ele aparece, usado para encontrar os autores com mais
  publicações.

As três últimas estruturas (citacoes, palavra_artigos e autor_contagem)
são índices auxiliares, mantidos consistentes a cada inserção, remoção ou
alteração de um artigo, de modo a tornar as consultas eficientes.
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
    dados = colecao.artigos.get(id_artigo)
    return dados["titulo"] if dados is not None else None


def _normalizar_palavras(palavras):
    return sorted({palavra for palavra in palavras if palavra})


def _normalizar_referencias(referencias):
    return sorted(set(referencias))


def _remover_dos_indices(colecao, id_artigo):
    dados = colecao.artigos[id_artigo]
    for autor in set(dados["autores"]):
        colecao.autor_contagem[autor] -= 1
        if colecao.autor_contagem[autor] == 0:
            del colecao.autor_contagem[autor]
    for palavra in dados["palavras"]:
        if palavra in colecao.palavra_artigos:
            colecao.palavra_artigos[palavra].discard(id_artigo)
    for referencia in dados["referencias"]:
        if referencia in colecao.citacoes:
            colecao.citacoes[referencia].discard(id_artigo)


def _adicionar_aos_indices(colecao, id_artigo, autores, palavras, referencias):
    for autor in set(autores):
        colecao.autor_contagem[autor] = colecao.autor_contagem.get(autor, 0) + 1
    for palavra in palavras:
        colecao.palavra_artigos[palavra].add(id_artigo)
    for referencia in referencias:
        colecao.citacoes[referencia].add(id_artigo)


def _definir_artigo(colecao, id_artigo, titulo, autores, ano, palavras, referencias):
    if id_artigo in colecao.artigos:
        _remover_dos_indices(colecao, id_artigo)
        del colecao.artigos[id_artigo]

    palavras_ordenadas = _normalizar_palavras(palavras)
    referencias_ordenadas = _normalizar_referencias(referencias)

    colecao.artigos[id_artigo] = {
        "titulo": titulo,
        "autores": list(autores),
        "palavras": palavras_ordenadas,
        "ano": ano,
        "referencias": referencias_ordenadas,
    }
    _adicionar_aos_indices(colecao, id_artigo, autores, palavras_ordenadas, referencias_ordenadas)


def carregar_arquivo(colecao, nome_arquivo):
    with open(nome_arquivo, encoding="utf-8") as arquivo:
        lista_artigos = json.load(arquivo)

    for dados in lista_artigos:
        _definir_artigo(
            colecao,
            dados["id"],
            dados["titulo"],
            dados["autores"],
            dados["ano"],
            dados["palavras-chave"],
            dados["referencias"],
        )


def obter_numero_artigos(colecao):
    return len(colecao.artigos)


def obter_palavras(colecao):
    return sorted(palavra for palavra, ids in colecao.palavra_artigos.items() if ids)


def obter_principais_autores(colecao):
    if not colecao.autor_contagem:
        return 0, []
    maximo = max(colecao.autor_contagem.values())
    autores = sorted(autor for autor, n in colecao.autor_contagem.items() if n == maximo)
    return maximo, autores


def obter_referencias_orfas(colecao):
    return sorted(
        id_referencia
        for id_referencia, citantes in colecao.citacoes.items()
        if citantes and id_referencia not in colecao.artigos
    )


def buscar_citacoes(colecao, id_artigo):
    return colecao.citacoes.get(id_artigo, set())


def buscar_palavras(colecao, consulta):
    cache = {}
    resultado = set()
    for grupo in consulta:
        conjunto_grupo = None
        for palavra in grupo:
            if palavra not in cache:
                cache[palavra] = colecao.palavra_artigos.get(palavra, set())
            ids_palavra = cache[palavra]
            if conjunto_grupo is None:
                conjunto_grupo = set(ids_palavra)
            else:
                conjunto_grupo &= ids_palavra
            if not conjunto_grupo:
                break
        if conjunto_grupo:
            resultado |= conjunto_grupo
    return resultado


def inserir_artigo(colecao, id_artigo, titulo, autores, ano, palavras, referencias):
    if id_artigo in colecao.artigos:
        return False
    _definir_artigo(colecao, id_artigo, titulo, autores, ano, palavras, referencias)
    return True


def remover_artigo(colecao, id_artigo):
    if id_artigo not in colecao.artigos:
        return False
    _remover_dos_indices(colecao, id_artigo)
    del colecao.artigos[id_artigo]
    return True


def alterar_palavras(colecao, id_artigo, palavras_novas):
    if id_artigo not in colecao.artigos:
        return False
    dados = colecao.artigos[id_artigo]
    for palavra in dados["palavras"]:
        if palavra in colecao.palavra_artigos:
            colecao.palavra_artigos[palavra].discard(id_artigo)

    palavras_ordenadas = _normalizar_palavras(palavras_novas)
    dados["palavras"] = palavras_ordenadas
    for palavra in palavras_ordenadas:
        colecao.palavra_artigos[palavra].add(id_artigo)
    return True


def alterar_referencias(colecao, id_artigo, referencias_novas):
    if id_artigo not in colecao.artigos:
        return False
    dados = colecao.artigos[id_artigo]
    for referencia in dados["referencias"]:
        if referencia in colecao.citacoes:
            colecao.citacoes[referencia].discard(id_artigo)

    referencias_ordenadas = _normalizar_referencias(referencias_novas)
    dados["referencias"] = referencias_ordenadas
    for referencia in referencias_ordenadas:
        colecao.citacoes[referencia].add(id_artigo)
    return True


def gravar_arquivo(colecao, nome_arquivo):
    lista_artigos = [
        {
            "id": id_artigo,
            "titulo": dados["titulo"],
            "autores": dados["autores"],
            "palavras-chave": dados["palavras"],
            "ano": dados["ano"],
            "referencias": dados["referencias"],
        }
        for id_artigo, dados in colecao.artigos.items()
    ]

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(lista_artigos, arquivo, indent=2, ensure_ascii=False)