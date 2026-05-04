nome_arquivo = input()
tamanho = int(input())

with open(nome_arquivo) as f:
    texto = f.read