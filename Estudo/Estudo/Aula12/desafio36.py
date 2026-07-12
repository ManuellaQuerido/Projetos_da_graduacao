''' 
Problema: averiguar se o comprador deve ter o pedido do emprétimo bancário aprovado

algoritmo:
    leia o valor da casa
    leia o salário do comprador
    leia o tempo em anos que ele vai pagar

    calcular a prestação mensal (valor da casa/(ano * 12)) e guardar em uma variável prest_m
    
    Se a prest_m for maior que o salário vezes 0,3:
        imprima "Empréstimo negado"
    Senão:
        imprima "Empréstimo aprovado"
'''

v_casa = float(input())
salário = float(input())
tempo = float(input())

prest_m = v_casa/(tempo * 12)

if prest_m > (salário * 0.3):
    print("Empréstimo negado")
else:
    print("Empréstimo aprovado")