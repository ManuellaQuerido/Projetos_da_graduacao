def maximo(lista, n):
    if n == 1:      # Caso base
        return lista[0]

    maior = maximo(lista, n - 1)

    if lista[n - 1] > maior:
        return lista[n - 1]
    else:
        return maior

def main():
    lista = list(map(int, input().split()))
    n = len(lista)

    resultado = maximo(lista, n)
    print(resultado)

main()