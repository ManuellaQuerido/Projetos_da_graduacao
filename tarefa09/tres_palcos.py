def main():
    n = int(input())
    shows = []
    duracao = []

    for i in range(n):
        linha = input().split()
        nome = linha[0]
        duracao_show = int(linha[1])
        shows.append(nome)
        duracao.append(duracao_show)