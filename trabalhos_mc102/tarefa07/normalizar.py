from funcoes import ler_pixels, achar_menor_maior, normalizar, contar
def main():

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

    pixels = ler_pixels(linhas)

    menor, maior = achar_menor_maior(pixels)

    pretos1, brancos1 = contar(pixels)

    novos = normalizar(pixels, menor, maior)

    pretos2, brancos2 = contar(novos)

    # escreve arquivo
    print("P2", file=novo_arq)
    print(comentario, end="", file=novo_arq)
    print(tamanho, end="", file=novo_arq)
    print("255", file=novo_arq)

    indice = 0

    for i in range(altura):

        for j in range(largura):

            print(novos[indice], end=" ", file=novo_arq)

            indice += 1

        print(file=novo_arq)

    # saída
    print(f"{entrada}: {pretos1} pixels pretos e {brancos1} pixels brancos")
    print(f"{saida}: {pretos2} pixels pretos e {brancos2} pixels brancos")

main()