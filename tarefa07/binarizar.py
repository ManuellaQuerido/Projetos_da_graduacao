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

entrada = input()
saida = input()

dados = input().split()

janela = int(dados[0])
limiar = int(dados[1])
fator = float(dados[2])

arq = open(entrada, "r")
novo_arq = open(saida, "w")

linhas = []

for linha in arq:
    linhas.append(linha)

comentario = linhas[1]
tamanho = linhas[2]

partes = tamanho.split()

largura = int(partes[0])
altura = int(partes[1])

pixels = ler_pixels(linhas)

pretos1, brancos1 = contar(pixels)

menor, maior = achar_menor_maior(pixels)

normalizada = normalizar(pixels, menor, maior)

binaria = binarizar(normalizada, largura, altura, janela, limiar, fator)

pretos2, brancos2 = contar(binaria)


print("P2", file=novo_arq)
print(comentario, end="", file=novo_arq)
print(tamanho, end="", file=novo_arq)
print("255", file=novo_arq)

indice = 0

for i in range(altura):

    for j in range(largura):

        print(binaria[indice], end=" ", file=novo_arq)

        indice += 1

    print(file=novo_arq)

print(f"{entrada}: {pretos1} pixels pretos e {brancos1} pixels brancos")
print(f"{saida}: {pretos2} pixels pretos e {brancos2} pixels brancos")  