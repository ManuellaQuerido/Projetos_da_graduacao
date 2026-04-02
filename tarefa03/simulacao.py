import math

tb = input()
t = int(input())
T = float(input())
w = float(input())
p = int(input())

a = 0.97
b = 1.6*((10**-10))
print(f"Após 0 minutos: {p}")

if tb == "Psicrófilos":
    Tidp = 10
    rp = 1.03526 * math.exp(-((T - Tidp)**2) / (Tidp**2))

    r = rp
    ti = 0
    tf = ti + 1

    while ti <= t:
        if w >= 1:
            p = int(p * r)
        else:
            p = int(p * w * r)

        if a * w >= b * p:
            w = (a * w) - (b * p)
        else:
            w = 0
        
        if p <= 0:
            print("População extinta")
            break
        print(f"Após {tf} minutos: {p}")
        tf += 1

if tb == "Mesófilos":
    Tidm = 35
    rm = 1.03526 * math.exp(-((T - Tidm)**2) / (Tidm**2))

    r = rm
    ti = 0
    tf = ti + 1

    while ti <= t:
        if w >= 1:
            p = int(p * r)
        else:
            p = int(p * w * r)

        if a * w >= b * p:
            w = (a * w) - (b * p)
        else:
            w = 0
        
        if p <= 0:
            print("População extinta")
            break
        print(f"Após {tf} minutos: {p}")
        tf += 1

if tb == "Termófilo":
    Tidt = 75
    rt = 1.03526 * math.exp(-((T - Tidt)**2) / (Tidt**2))
   
    r = rt
    ti = 0
    tf = ti + 1

    while ti <= t:
        if w >= 1:
            p = int(p * r)
        else:
            p = int(p * w * r)

        if a * w >= b * p:
            w = (a * w) - (b * p)
        else:
            w = 0
        
        if p <= 0:
            print("População extinta")
            break
        print(f"Após {tf} minutos: {p}")
        tf += 1