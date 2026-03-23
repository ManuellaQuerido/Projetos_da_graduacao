tb = str(input("Insira o tipo de bactéria: "))
    print(tb)
T = float(input("Insira a temperatura do ambiente em graus celsios: "))
    print(T)

if tb == psicrófilos:
    Topt = 10
    Tmin = 0
    Tmax = 20
if tb == mesófilos:
    Topt = 35°C
    Tmin = 20°C
    Tmax = 50°C
if tb == termófilo:
    Topt = 75°C
    Tmin = 50°C
    Tmax = 100°C

if T < Tmin
    print("Temperatura muito baixa, aqueça a incubadora.")
else T > Tmax
    print("Temperatura muito alta, resfrie a incubadora.")
