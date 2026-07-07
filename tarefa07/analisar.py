from funcoes import ler_pixels, achar_menor_maior, normalizar, binarizar, contar_disco

def main():

    entrada = input()

    dados = input().split()

    janela = int(dados[0])
    limiar = int(dados[1])
    fator = float(dados[2])

    dados_disco = input().split()

    x = float(dados_disco[0])
    y = float(dados_disco[1])
    raio = float(dados_disco[2])

    media = int(input())

    # abre arquivo

    arq = open(entrada, "r")

    linhas = []

    for linha in arq:
        linhas.append(linha)

    # largura e altura

    tamanho = linhas[2].split()

    largura = int(tamanho[0])
    altura = int(tamanho[1])

    # lê pixels

    pixels = ler_pixels(linhas)

    # normaliza

    menor, maior = achar_menor_maior(pixels)

    normalizada = normalizar(pixels, menor, maior)

    # binariza

    binaria = binarizar(normalizada, largura, altura, janela, limiar, fator)

    # conta pretos dentro do disco

    pixels_pretos = contar_disco(binaria, largura, altura, x, y, raio)

    # estima colônias
    colonias = pixels_pretos // media

    # saída

    print(f"Número de colônias estimado: {colonias}")

    if colonias < 30:
        print("Placa inadequada, dilua menos a amostra.")

    elif colonias > 300:
        print("Placa inadequada, dilua mais a amostra.")

    else:
        print("Placa adequada para contagem.")

main()