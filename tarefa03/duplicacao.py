tb = input("Tipo de bactéria: ")
T = float(input("Temperatura ambiente: "))

if tb == "psicrófilos" or tb == "mesófilos" or tb == "termófilo":
    if tb == "psicrófilos" and T == 10:
        print("Temperatura ideal")
    else:
        if  tb == "psicrófilos" and T > 20:
            print("Temperatura muito alta, resfrie a incubadora.")
        if  tb == "psicrófilos" and T < 0:
            print("Temperatura muito baixa, esquente a incubadora")
        if tb == "psicrófilos" and T <= 20 and T >= 0:
            print("Intervalo de temperatura OK!")

    if tb == "mesófilos" and T == 35:
        print("Temperatura ideal")
    else:
        if tb == "mesófilos" and T > 50:
            print("Temperatura muito alta, resfrie a incubadora.")
        if tb == "mesófilos" and T < 20:
            print("Temperatura muito baixa, esquente a incubadora")
        if tb == "mesófilos" and T <= 50 and T >= 20:
            print("Intervalo de temperatura OK!")

    if tb == "termófilo" and T == 75:
        print("Temperatura ideal")
    else:
        if tb == "termófilo" and T > 100:
            print("Temperatura muito alta, resfrie a incubadora.")
        if tb == "termófilo" and T < 50:
            print("Temperatura muito baixa, esquente a incubadora")
        if tb == "temófilo" and T <= 100 and T >= 50:
            print("Intervalo de temperatura OK!")
else:
    print("Tipo de bactéria ou temperatura inválidos")