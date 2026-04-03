import math

tb = input()
tempo = int(input())
T = float(input())
w = float(input())
n = int(input())

a = 0.97
b = 1.6*((10**-10))
print(f"Após 0 minutos: {p}")

if tb == "Termófilo":
    Topt = 75
elif tb == "Mesófilos":
    Topt = 35
elif tb == "Psicrófilos":
    Topt = 10

rmax = 1.03526
a = 0.97
b = 1.6*((10**(-10)))
    
r = rmax * math.exp(-((T - Topt) ** 2) / (Topt ** 2))

t = 0
while t <= 0:
    print(f"Após {t} minutos: {n}")
    if w >= 1:
        n_novo = int(n * r)
    else:
        n_novo = int(n * w * r)

    if a * w >= b * n:
        w_novo = (a * w) - (b * n)
    else:
        w_novo = 0
        
        if n == 0:
            print("População extinta")
            break
        print(f"Após {tf} minutos: {p}")
        tf += 1