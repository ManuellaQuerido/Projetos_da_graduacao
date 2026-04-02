import math # Importa funções de matemática

# Entrada do tipo de bactéria e da temperatura ambiente
tb = input()
T = float(input())

Tm, TM, Topt = 0, 0, 0

# Temperaturas mínimas (Tm), máximas (TM) e a ideal (Topt)
if tb == "Termófilo":
    Tm, TM, Topt = 50, 100, 75
elif tb == "Psicrófilos":
    Tm, TM, Topt = 0, 20, 10
elif tb == "Mesófilos":
    Tm, TM, Topt = 20, 50, 35

print("Tipo de bactéria: Temperatura ambiente:")
# Se a temperatura for maior ou menor que TM e Tm, respectivamente. Senão, execute a função para encontrar a taxa de crescimento por minuto.
if T < Tm:
    print("Temperatura muito baixa, aqueça a incubadora.")
elif T > TM:
    print("Temperatura muito alta, resfrie a incubadora.")
else:
    rmax = 1.03526
    r = rmax * math.exp(-((T - Topt) ** 2) / (Topt ** 2))
    print(f"Taxa de crescimento por minuto: {r:.4f}")

    if r <= 1:
        print("Não há crescimento exponecial, ajuste a temperatura.")
    else:
        tempo = math.log(2) / math.log(r)
        print(f"Tempo de duplicação:{tempo:.1f} minutos")
