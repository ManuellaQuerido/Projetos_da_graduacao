nome_arq = input()
carros, dinos = {}, {}

try:
    f = open(nome_arq, "r")
    for linha in f:
        linha = linha.replace("\n", "").replace("\r", "")
        if not linha: continue
        p = linha.split(",")
        # Pega a hora cheia (ex: 12h)
        hora = p[0].split("h")[0] + "h"
        cat = p[2]
        valor = float(p[3])
        
        if "carro" in cat:
            carros[hora] = carros.get(hora, 0.0) + valor
        else:
            dinos[hora] = dinos.get(hora, 0.0) + valor
    f.close()
except:
    pass

def exibir(titulo, dicionario):
    if not dicionario: return
    # Converter para lista e ordenar: Valor desc, Hora asc
    lista = []
    for h in dicionario:
        lista.append([h, dicionario[h]])
    
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][1] < lista[j+1][1] or (lista[j][1] == lista[j+1][1] and lista[j][0] > lista[j+1][0]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    print(f"{titulo}:")
    for item in lista:
        print(f"{item[0]}: {item[1]:.2f}")
    print()

exibir("Carros", carros)
exibir("Dinossauros", dinos)