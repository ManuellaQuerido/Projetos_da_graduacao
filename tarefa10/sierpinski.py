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


def desenhar(matriz, n, linha, coluna):
    
    if n == 1:

        matriz[linha][coluna + 1] = "/"
        matriz[linha][coluna + 2] = "\\"
        matriz[linha + 1][coluna] = "/"
        matriz[linha + 1][coluna + 1] = "_"
        matriz[linha + 1][coluna + 2] = "_"
        matriz[linha + 1][coluna + 3] = "\\"
        
        return

    tamanho = 2 ** (n - 1)

    desenhar(matriz, n - 1, linha, coluna + tamanho)
    desenhar(matriz, n - 1, linha + tamanho, coluna)
    desenhar(matriz, n - 1, linha + tamanho, coluna + 2 * tamanho)


def main():
    
    n = int(input())

    matriz = sierpinski_formatado(n)

    for linha in matriz:
        print(linha)

main()