import telemetria

def calcular_distancia_total(leituras):
    total = 0.0

    for i in range(len(leituras) - 1):
        t1, x1, y1 = leituras[i]
        t2, x2, y2 = leituras[i + 1]

        total += telemetria.distancia(x1, y1, x2, y2)
    
    return total

def calcular_velocidades(leituras):
    velocidades = []

    for i in range(len(leituras) - 1):
        t1, x1, y1 = leituras[i]
        t2, x2, y2 = leituras[i + 1]

        d = telemetria.distancia(x1, y1, x2, y2 )
        dt = t2 - t1

        velocidades.append(d / dt)

    return velocidades

def imprimir_relatorio(total, dist_inicio, vmax, var_max, dist_destino, prox_x, prox_y):
    print(f"Distância total percorrida: {total:.2f}")
    print(f"Distância ao ponto de partida: {dist_inicio:.2f}")
    print(f"Velocidade máxima: {vmax:.2f}")
    print(f"Variação máxima de velocidade: {var_max:.2f}")
    print(f"Distância ao destino: {dist_destino:.2f}")
    print(f"Próxima posição estimada: {prox_x:.2f} {prox_y:.2f}")

def main():
    v_max, leituras = telemetria.ler_trajetoria()

    dados = input().split()
    x = float(dados[0])
    y = float(dados[1])

    corrompidas = telemetria.detectar_corrompidas(leituras, v_max)
    corrigidas = telemetria.reconstruir(leituras, corrompidas)
    