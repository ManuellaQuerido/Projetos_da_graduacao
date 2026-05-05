nome_arquivo = input()
tamanho = int(input())

with open(nome_arquivo) as f:
    linha_atual = ""

    for linha in f:
        if linha == "\n": #fim do parágrafo
            if linha_atual != " ":
                espacos = tamanho - len(linha_atual)
                