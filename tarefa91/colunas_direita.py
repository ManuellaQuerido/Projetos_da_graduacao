nome_arquivo = input()

valores = input().split()
maximo_caracteres = int(valores[0])
maximo_linhas = int(valores[1])

tamanho = int(input())

linhas_formatadas = []

with open(nome_arquivo) as f:
    linha_atual = ""