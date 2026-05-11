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