def busca_binária(sequencia, x):
    if len(sequencia) == 0:
        return False

    meio = len(sequencia) // 2

    if sequencia[meio] == x:
        return True
    elif x < sequencia[meio]:
        return busca_binária(sequencia[:meio], x)
    else:
        return busca_binária(sequencia[meio + 1:], x)

def main():
    sequencia = list(map(int, input().split()))
    x = int(input())

    resultado = busca_binária(sequencia, x)
    print(resultado)

main()