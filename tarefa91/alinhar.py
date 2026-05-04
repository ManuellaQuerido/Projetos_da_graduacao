nome_arquivo = input()
tamanho = int(input())

with open(nome_arquivo) as f:
    texto = f.read()

palavras = texto.split()

linhas = []
linha_atual = ""

for palavra in palavras:
    if linha_atual == " ":
        novo = palavra
    else:
        novo = linha_atual + " " + palavra

    if len(novo) <= tamanho:
        linha_atual = novo
    else:
        linhas.append(linha_atual)
        linha_atual = palavra

if linha_atual != " ":
    linhas.append(linha_atual)

for linha in linhas:
    espacos = tamanho - len(linha)
    print(" " * espacos + linha)