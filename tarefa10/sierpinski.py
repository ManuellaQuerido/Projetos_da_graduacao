def sierpinski(n):
    altura = 2 ** n
    largura = 2 ** (n + 1)

    matriz = []

    for i in range(altura):
        linha = []
        for j in range(largura):
            linha.append(" ")
        matriz.append(linha)

    desenhar(matriz, n, 0, 0)
    return matriz





def main():



main()