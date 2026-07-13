def menor_cofator(matriz, i, j):
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


def main():
    n = int(input())
    matriz = []
    for i in range(n):
        linha = list(map(int, input().split()))
        matriz.append(lista)

    resultado = det(matriz)
    print(f"{resultado:.2f}")    

main()