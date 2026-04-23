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

    total = calcular_distancia_total(corrigidas)

    x0, y0 = corrigidas[0][1], corrigidas[0][2]
    xn, yn = corrigidas[-1][1], corrigidas[-1][2]

    dist_inicio = telemetria.distancia(x0, y0, xn, yn)

    velocidades = calcular_velocidades(corrigidas)

    vmax_calc = max(velocidades)
    var_max = telemetria.max_variacao(velocidades)

    dist_destino = telemetria.distancia(xn, yn, xd, yd)

    x_prev, y_prev = corrigidas[-2][1], corrigidas[-2][2]
    prox_x = xn + (xn - x_prev)
    prox_y = yn + (yn - y_prev)

    imprimir_relatorio(total, dist_inicio, vmax_calc, var_max, dist_destino, prox_x, prox_y)

if __name__ == "__main__":
    main()