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
        