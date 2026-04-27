nome_arq = input()
carros = {}
dinos = {}

f = open(nome_arq, "r")
for linha in f:
    if linha[-1] == "\n": linha = linha[:-1]
    if not linha: continue
    p = linha.split(",")
    hora_cheia = p[0].split("h")[0] + "h"
    valor = float(p[3])
    
    dicionario = carros if p[2] == "carro" else dinos
    dicionario[hora_cheia] = dicionario.get(hora_cheia, 0.0) + valor
f.close()

def processar(titulo, dados):
    if not dados: return

    lista = [[h, v] for h, v in dados.items()]

    for i in range(len(lista)):
        for j in range(len(lista)-1-i):
            if lista[j][1] < lista[j+1][1] or (lista[j][1] == lista[j+1][1] and lista[j][0] > lista[j+1][0]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    print(f"{titulo}:")
    for h, v in lista:
        print(f"{h}: {v:.2f}")
    print()

processar("Carros", carros)
processar("Dinossauros", dinos)