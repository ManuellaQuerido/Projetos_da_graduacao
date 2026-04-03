import math

tb = input()
tempo_final = int(input())
T = float(input())
w = float(input())
n = int(input())

a = 0.97
b = 1.6*((10**-10))

if tb == "Termófilo":
    Topt = 75
elif tb == "Mesófilos":
    Topt = 35
elif tb == "Psicrófilos":
    Topt = 10

rmax = 1.03526
r = rmax * math.exp(-((T - Topt) ** 2) / (Topt ** 2))

tempo = 0
while tempo <= tempo_final:
    print(f"Após {tempo} minutos: {n}")
    if w >= 1:                      #calculo para o n_novo, ou seja, a nova população de bactérias
        n_novo = int(n * r)
    else:
        n_novo = int(n * w * r)

    if a * w >= b * n:              #Calculo para o w_novo, ou seja, a taxa de crescimento populacional
        w_novo = (a * w) - (b * n)
    else:
        w_novo = 0
        
    n = n_novo
    w = w_novo

    if n == 0:
        print("População extinta")
        break

    tempo += 1