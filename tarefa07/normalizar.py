def ler_pixels(linhas):

    pixels = []

    for i in range(4, len(linhas)):

        valores = linhas[i].split()

        for v in valores:
            pixels.append(int(v))

    return pixels


def achar_menor_maior(pixels):

    menor = pixels[0]
    maior = pixels[0]

    for p in pixels:

        if p < menor:
            menor = p

        if p > maior:
            maior = p

    return menor, maior


def normalizar(pixels, menor, maior):

    novos = []

    for p in pixels:

        if maior == menor:
            valor = 0

        else:
            valor = ((p - menor) * 255) // (maior - menor)

        novos.append(valor)

    return novos


def contar(pixels):

    pretos = 0
    brancos = 0

    for p in pixels:

        if p == 0:
            pretos += 1

        if p == 255:
            brancos += 1

    return pretos, brancos


entrada = input()
saida = input()

arq = open(entrada, "r")
novo_arq = open(saida, "w")

linhas = []

for linha in arq:
    linhas.append(linha)

tipo = linhas[0]
comentario = linhas[1]
tamanho = linhas[2]

partes = tamanho.split()

largura = int(partes[0])
altura = int(partes[1])