def busca_binária(sequencia, x):
    
    if len(sequencia) == 0: # Caso base para lista vazia
        return 0

    if len(sequencia) == 1: # Caso base para lista com uma entrada
        if sequencia[0] == x:
            return 1
        return 0

    meio = len(sequencia) // 2

    prim_metade = busca_binária(sequencia[:meio], x)
    seg_metade = busca_binária(sequencia[meio:], x)

    return prim_metade + seg_metade

def main():
    sequencia = list(map(int, input().split()))
    x = int(input())

    resultado = busca_binária(sequencia, x)
    print(resultado)

main()