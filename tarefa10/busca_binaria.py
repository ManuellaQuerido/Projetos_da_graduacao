def busca_binária(sequencia, x):
    if len(sequencia) == 0:
        return False

def main():
    sequencia = list(map(input().strip().split()))
    x = int(input())

    resultado = busca_binária(sequencia, x)
    print(resultado)

main()