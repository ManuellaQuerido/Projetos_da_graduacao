def adicionar(horas, valores, hora, valor):
    achou = False

    for i in range(len(horas)):
        
        if horas[i] == hora:
            valores[i] += valor
            achou = True
    
    if achou == False:
        horas.append(hora)
        valores.append(valor)


def ordenar(horas, valores):
    for i in range(len(valores)):
        maior = i
        for j in range(i+1, len(valores)):

            if valores[j] > valores[maior]:
                maior = j

            elif valores[j] == valores[maior]:
                if horas[j] < horas[maior]:
                    maior = j

        temp = valores[i]
        valores[i] = valores[maior]
        valores[maior] = temp

        temp = horas[i]
        horas[i] = horas[maior]
        horas[maior] = temp


def main():
    arquivo = input()
    horas_carro = []
    valores_carro = []
    horas_dinossauro = []
    valores_dinossauro = []

    with open(arquivo) as pasta:
        for linha in pasta:
            dados = linha.split(",")

            hora = dados[0][:2] + "h"
            categoria = dados[2]
            valor = float(dados[3])

            if categoria == "carro":
                adicionar(horas_carro, valores_carro, hora, valor)
            else:
                adicionar(horas_dinossauro, valores_dinossauro, hora, valor)
    
    ordenar(horas_carro, valores_carro)
    ordenar(horas_dinossauro, valores_dinossauro)

    print("Carros:")
    for i in range(len(horas_carro)):
        print(f"{horas_carro[i]}: {valores_carro[i]:.2f}")
    
    print()

    print ("Dinossauros:")
    for i in range(len(horas_dinossauro)):
        print(f"{horas_dinossauro[i]}: {valores_dinossauro[i]:.2f}")

main()