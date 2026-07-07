from funcoes import ler_pixels, achar_menor_maior, normalizar, binarizar, contar
def main():

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

main()