def maximo(lista, n):
    if n == 1:      # Caso base
        return lista[0]
    
    if n == 2:
        if lista[0] >= lista[1]:
            return lista[0]
        else:
            return lista[1]

def main():
    lista = list(map(int, input().split()))
    n = len(lista)
    
    print(resultado)


main()