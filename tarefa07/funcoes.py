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



def binarizar(pixels, largura, altura, janela, limiar, fator):

    resultado = []

    raio = janela // 2

    for i in range(altura):

        for j in range(largura):

            contagem = 0

            for di in range(-raio, raio + 1):

                for dj in range(-raio, raio + 1):

                    ni = i + di
                    nj = j + dj
                    
                    if ni >= 0 and ni < altura and nj >= 0 and nj < largura:

                        indice = ni * largura + nj

                        if pixels[indice] <= limiar:
                            contagem += 1

            total = janela * janela

            if contagem >= fator * total:
                resultado.append(0)

            else:
                resultado.append(255)

    return resultado


def contar_disco(imagem, largura, altura, x, y, raio): #função adicionada

    pretos = 0

    for i in range(altura):
        dy = altura - 1 - i - y

        for j in range(largura):
            dx = j - x

            if dx ** 2 + dy ** 2 <= raio * raio:

                indice = i * largura + j

                if imagem[indice] == 0:
                    pretos += 1

    return pretos