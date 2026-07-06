NOTA_MINIMA = 5.0

def obter_maximo(lista):
    assert lista, "Lista não pode ser vazia"
    maximo = lista[0]
    for valor in lista:
        if maximo < valor:
            maximo = valor
    breakpoint()
    return maximo

def multiplicar_fator(lista, fator):
    n = len(lista)
    for i in range(n):
        lista[i] = lista[i] * fator

def ler_lista_notas():
    n = int(input("Digite o número de estudantes: "))
    lista_notas = []
    for _ in range(n):
        lista_notas.append(float(input()))
    return lista_notas

def imprimir_lista_aprovacao(lista_notas):
    for nota in lista_notas:
        if nota < NOTA_MINIMA:
            print("reprovado")
        else:
            print("aprovado")

def main():
    lista_notas = ler_lista_notas()

    maximo = obter_maximo(lista_notas)
    fator = 10.0 / maximo
    multiplicar_fator(lista_notas, fator)

    imprimir_lista_aprovacao(lista_notas)

main()