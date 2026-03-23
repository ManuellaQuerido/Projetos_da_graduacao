tb = input("Tipo de bactéria: ")
T = float(input("Temperatura ambiente: "))

if tb == psicrófilos:
    if T >= 20:
        print("Temperatura muito alta, resfrie a incubadora.")
    if T <= 0:
        print("Temperatura muito baixa, esquente a incubadora")
    if T == 10:
        print("Temperatura ideal")

if tb == mesófilos:
    if T >= 50:
        print("Temperatura muito alta, resfrie a incubadora.")
     if T <= 20:
        print("Temperatura muito baixa, esquente a incubadora")
    if T == 35:
        print("Temperatura ideal")

if tb == termófilo:
    if T >= 100:
        print("Temperatura muito alta, resfrie a incubadora.")
     if T <= 50:
        print("Temperatura muito baixa, esquente a incubadora")
    if T == 75:
        print("Temperatura ideal")
