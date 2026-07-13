def menor_comple(matriz, i, j):
    n = len(matriz)
    menor = []
    for linha in range(n):
        if linha != i:
            nova_linha = []
            for coluna in range(n):
                if coluna != j:
                    nova_linha.append(matriz[linha][coluna])
            menor.append(nova_linha)
    return menor

def det(matriz):
    n = len(matriz)

    if n == 1:          # Caso base -> matriz 1x1
        return float(matriz[0][0])
    
    if n == 2:          # Caso base -> matriz 2x2
        m1 = float(matriz[0][0] * matriz [1][1])
        m2 = float(matriz[0][1] * matriz[1][0])

        return m1 - m2

    resultado = 0.0
    for j in range(n):
        menor = menor_comple(matriz, 0, j)
        cofator = ((-1) ** (0 + j)) * det(menor)
        resultado += matriz[0][j] * cofator
    return resultado


def main():
    n = int(input())
    matriz = []
    for i in range(n):
        linha = list(map(float, input().split()))
        matriz.append(linha)

    resultado = det(matriz)
    print(f"{resultado:.2f}")    

main()