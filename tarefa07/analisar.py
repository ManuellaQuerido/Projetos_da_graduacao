#funções iguais a binarizar.py
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

        for j in range(largura):

            # centro do pixel
            px = j + 0.5
            py = altura - i - 0.5

            dx = px - x
            dy = py - y

            distancia2 = dx * dx + dy * dy

            if distancia2 <= raio * raio:

                indice = i * largura + j

                if imagem[indice] == 0:
                    pretos += 1

    return pretos


# programa principal

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
quociente = pixels_pretos // media
resto = pixels_pretos % media

if resto >= (media/2):
    colonias = quociente
else:
    if resto < (media / 2):
        colonias = quociente + 1

# saída

print(f"Número de colônias estimado: {colonias}")

if colonias < 30:
    print("Placa inadequada, dilua menos a amostra.")

elif colonias > 300:
    print("Placa inadequada, dilua mais a amostra.")

else:
    print("Placa adequada para contagem.")