import telemetria

def calcular_distancia_total(leituras):
    total = 0.0

    for i in range(len(leituras) - 1):
        t1, x1, y1 = leituras[i]
        t2, x2, y2 = leituras[i + 1]

        total += telemetria.distancia(x1, y1, x2, y2)
    
    return total