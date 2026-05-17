def ler_pixels(linhas):

    pixels = []

    for i in range(4, len(linhas)):

        valores = linhas[i].split()

        for v in valores:
            pixels.append(int(v))

    return pixels