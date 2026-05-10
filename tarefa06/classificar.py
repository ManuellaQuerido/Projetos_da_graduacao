nome_arquivo = input()

horas_carro = []
valores_carro = []

horas_dinossauro = []
valores_dinossauro = []

with open(nome_arquivo) as arquivo:
    for linha in arquivo:
        dados = linha.split(",")

        hora = dados[0][:2] + "h"
        catgoria = dados[2]
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