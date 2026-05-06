nome_arquivo = input()

valores = input().split()
maximo_caracteres = int(valores[0])
maximo_linhas = int(valores[1])

tamanho = int(input())

linhas_formatadas = []

with open(nome_arquivo) as f:
    linha_atual = ""

    for linha in f:
        if linha == "\n":
            if linha_atual != "":
                espacos = tamanho - len(linha_atual)
                linhas_formatadas.append(" " * espacos + linha_atual)
                linha_atual = ""
            linhas_formatadas.append("")
        else:
            palavras = linha.split()
            for palavra in palavras:
                if linha_atual == "":
                    novo = palavra
                else:
                    novo = linha_atual + " " + palavra
                if len(novo) <= tamanho:
                    linha_atual = novo
                else:
                    espacos = tamanho - len(linha_atual)
                    linhas_formatadas.append(" " * espacos + linha_atual)
                    linha_atual = palavra

    if linha_atual != "":
        espacos = tamanho - len(linha_atual)
        linhas_formatadas.append(" " * espacos + linha_atual)

linha_por_pagina = 2 * maximo_linhas
i = 0

while i < len(linhas_formatadas):
    pagina = linhas_formatadas[i:i + linha_por_pagina]
    i += linha_por_pagina

    coluna_1 = pagina[:maximo_linhas]
    coluna_2 = pagina[maximo_linhas:]

    while len(coluna_1) < maximo_linhas:
        coluna_1.append("")
    while len(coluna_2) < maximo_linhas:
        coluna_2.append("")