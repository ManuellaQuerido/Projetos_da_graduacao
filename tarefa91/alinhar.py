nome_arquivo = input()
tamanho = int(input())

with open(nome_arquivo) as f:
    linha_atual = ""

    for linha in f:
        if linha == "\n": #fim do parágrafo
            if linha_atual != " ":
                espacos = tamanho - len(linha_atual)
                print(" " * espacos + linha_atual)
                linha_atual = " "
            print()
        else:
            palavras = linha.split()
            for palavra in palavras:
                if linha_atual == " ":
                    novo = palavra
                else:
                    novo = linha_atual + " " + palavra

                if len(novo) <= tamanho:
                    linha_atual = novo
                else:
                    espacos = tamanho - len(linha_atual)
                    print(" " * espacos + linha_atual)
                    linha_atual = palavra

if linha_atual != " ":
    espacos = tamanho - len(linha_atual)
    print(" " * espacos + linha_atual)