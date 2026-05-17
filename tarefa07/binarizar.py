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