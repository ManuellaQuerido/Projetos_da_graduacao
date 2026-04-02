import math # Importa funções de matemática

# Entrada do tipo de bactéria e da temperatura ambiente
tb = input()
T = float(input())

# Temperaturas mínimas (Tm), máximas (TM) e a ideal (Topt)
if tb == "Psicrófilos":
    print(f"Tipo de bactéria: {tb} Temperatura ambiente: {T}")

    if T < 0:
        print("Temperatura muito baixa, aqueça a incubadora.")
    elif T > 20:
        print("Temperatura muito alta, resfrie a incubadora.")
    else:
        rmax = 1.03526
        r = rmax * math.exp(-((T - 10) ** 2) / (10 ** 2))
        print(f"Taxa de crescimento por minuto: {r:.4f}")

        if r <= 1:
            print("Não há crescimento exponecial, ajuste a temperatura.")
        else:
            tempo = math.log(2) / math.log(r)
            print(f"Tempo de duplicação: {tempo:.1f} minutos")

elif tb == "Mesófilos":
    print(f"Tipo de bactéria: {tb} Temperatura ambiente: {T}")

    if T < 20:
        print("Temperatura muito baixa, aqueça a incubadora.")
    elif T > 50:
        print("Temperatura muito alta, resfrie a incubadora.")
    else:
        rmax = 1.03526
        r = rmax * math.exp(-((T - 35) ** 2) / (35 ** 2))
        print(f"Taxa de crescimento por minuto: {r:.4f}")

        if r <= 1:
            print("Não há crescimento exponecial, ajuste a temperatura.")
        else:
            tempo = math.log(2) / math.log(r)
            print(f"Tempo de duplicação: {tempo:.1f} minutos")
            
elif tb == "Termófilo":
    print(f"Tipo de bactéria: {tb} Temperatura ambiente: {T}")

    if T < 50:
        print("Temperatura muito baixa, aqueça a incubadora.")
    elif T > 100:
        print("Temperatura muito alta, resfrie a incubadora.")
    else:
        rmax = 1.03526
        r = rmax * math.exp(-((T - 75) ** 2) / (75 ** 2))
        print(f"Taxa de crescimento por minuto: {r:.4f}")

        if r <= 1:
            print("Não há crescimento exponecial, ajuste a temperatura.")
        else:
            tempo = math.log(2) / math.log(r)
            print(f"Tempo de duplicação: {tempo:.1f} minutos")