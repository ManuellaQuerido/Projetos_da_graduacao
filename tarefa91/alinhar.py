nome_arquivo = input()
tamanho = int(input())

with open(nome_arquivo) as f:
    texto = f.read()

palavras = texto.split()

linhas = []
linha_atual = ""

for palavra in palavras:
    if linha_atual == "":
        novo = palavra
    else:
        novo = linha_atual + " " + palavra