import math # Importa funções de matemática

# Entrada do tipo de bactéria e da temperatura ambiente
tb = input()
T = float(input())

tb = tb.lower()
Tm, TM, Topt = 0, 0, 0
# Temperaturas mínimas (Tm), máximas (TM) e a ideal (Topt)
if tb in ["Psicrófilos", "Psicrofilos", "psicrófilos", "psicrofilos", "PSICRÓFILOS", "PSICROFILOS"]:
    Tm, TM, Topt = 0, 20, 10
elif tb in ["Mesófilos", "Mesofilos", "mesófilos", "mesofilos", "MESÓFILOS", "MESOFILOS":
    Tm, TM, Topt = 20, 50, 35
elif tb in ["Termófilo", "Termofilo", "termófilo", "termofilo", "TERMOFILO", "TERMÓFILO", "Termófilos", "Termofilos", "termófilos", "termofilos", "TERMOFILOS", "TERMÓFILOS"]:
    Tm, TM, Topt = 50, 100, 75
print("Tipo de bactéria: Temperatura ambiente:")

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
