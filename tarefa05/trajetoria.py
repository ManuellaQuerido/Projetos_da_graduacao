import telemetria


def imprimir_trajetoria(leituras_corrigidas):
    for t, x, y in leituras_corrigidas:
        print(f"{t:.0f} {x:.2f} {y:.2f}")


def main():
    v_max, leituras = telemetria.ler_trajetoria()
    corrompidas = telemetria.detectar_corrompidas(leituras, v_max)
    corrigidas = telemetria.reconstruir(leituras, corrompidas)
    imprimir_trajetoria(corrigidas)

if __name__ == "__main__":
    main()