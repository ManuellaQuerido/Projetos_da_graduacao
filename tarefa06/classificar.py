nome_arquivo = input()

horas_carro = []
valores_carro = []

horas_dinossauro = []
valores_dinossauro = []

with open(nome_arquivo) as arquivo:
    for linha in arquivo:
        dados = linha.split(",")

        hora = dados[0][:2] + "h"
        categoria = dados[2]
        valor = float(dados[3])

        if categoria == "carro":
            achou = False
            
            for i in range(len(horas_carro)):
                if horas_carro[i] == hora:
                    valores_carro[i] += valor
                    chou = True
            
            if achou == False:
                horas_carro.append(hora)
                valores_carro.append(valor)
        
        else:
            achou = False

            for i in range(len(horas_dinossauro)):
                if horas_dinossauro[i] == hora:
                    valores_dinossauro[i] += valor
                    achou = True
            
            if achou == False:
                horas_dinossauro.append(hora)
                valores_dinossauro.append(valor)
    
for i in range(len(valores_carro)):
    maior = i

    for j in range(i+1, len(valores_carro)):
        if valores_carro[j] > valores_carro[maior]:
            maior = j
            
        elif valores_carro[j] == valores_carro[maior]:
            if horas_carro[j] < horas_carro[maior]:
                maior = j
            
    temp = valores_carro[i]
    valores_carro[i] = valores_carro[maior]
    valores_carro = temp

    temp = horas_carro[i]
    horas_carro[i] = horas_carro[maior]
    horas_carro[maior] = temp

for i in range(len(valores_dinossauro)):
    maior = i

    for j in range(len(valores_dinossauro)):
        if valores_dinossauro[j] > valores_dinossauro[maior]:
            maior = j
        elif valores_dinossauro[j] == valores_dinossauro[maior]:
            if horas_dinossauro[j] < horas_dinossauro[maior]:
                maior[j]
    
    temp = valores_dinossauro[i]
    valores_dinossauro[i] = valores_dinossauro[maior]
    valores_dinossauro = temp

    temp = horas_dinossauro[i]
    horas_dinossauro[i] = horas_dinossauro[maior]
    horas_dinossauro[maior] = temp

print("Carros:")

for i in range(len(horas_carro)):
    print(f"{horas_carro[i]}: {valores_carro[i]:.2f}")
print()

print("Dinossauros:")

for i in range(len(horas_dinossauro)):
    print(f"{horas_dinossauro[i]}: {valores_dinossauro[i]:.2f}")