import math

tb = input("Tipo de bactéria: ")
T = float(input("Temperatura ambiente: "))

 # Programa que peça o nome da bactéria e o vlor da temperatura ambiente
if tb == "psicrófilos" or tb == "mesófilos" or tb == "termófilo":
    if tb == "psicrófilos" and T == 10:
        print("Temperatura ideal")
    else:
        if  tb == "psicrófilos" and T > 20:
            print("Temperatura muito alta, resfrie a incubadora.")
        if  tb == "psicrófilos" and T < 0:
            print("Temperatura muito baixa, esquente a incubadora")
    if tb == "psicrófilos" and T <= 20 and T >= 0 or T == 10:
        Tidp = 10
        rp = 1.03526 * math.exp(-((T - Tidp)**2) / (Tidp**2))
        
        print(f"Taxa de crescimento por minuto: {rp}")

        if rp <= 1:
            print("Não há crescimento exponencial, ajuste a temperatura")
        else:
            t = math.log(2) / math.log(rp)
            print(f"Tempo de duplicação: {t}")

    if tb == "mesófilos" and T == 35:
        print("Temperatura ideal")
    else:
        if tb == "mesófilos" and T > 50:
            print("Temperatura muito alta, resfrie a incubadora.")
        if tb == "mesófilos" and T < 20:
            print("Temperatura muito baixa, esquente a incubadora")
    if tb == "mesófilos" and T <= 50 and T >= 20 or T == 35:
        Tidm = 35
        rm = 1.03526 * math.exp(-((T - Tidm)**2) / (Tidm**2))
      
        print(f"Taxa de crescimento por minuto: {rm}")

        if rm <= 1:
            print("Não há crescimento exponencial, ajuste a temperatura")
        else:
            t = math.log(2) / math.log(rm)
            print(f"Tempo de duplicação: {t}")

    if tb == "termófilo" and T == 75:
        print("Temperatura ideal")
    else:
        if tb == "termófilo" and T > 100:
            print("Temperatura muito alta, resfrie a incubadora.")
        if tb == "termófilo" and T < 50:
            print("Temperatura muito baixa, esquente a incubadora")
    if tb == "termófilo" and T <= 100 and T >= 50 or T == 75:
        Tidt = 75
        rt = 1.03526 * math.exp(-((T - Tidt)**2) / (Tidt**2))
      
        print(f"Taxa de crescimento por minuto: {rt}")

        if rt <= 1:
            print("Não há crescimento exponencial, ajuste a temperatura")
        else:
            t = math.log(2) / math.log(rt)
            print(f"Tempo de duplicação: {t}")

else:
    print("Tipo de bactéria ou temperatura inválidos")