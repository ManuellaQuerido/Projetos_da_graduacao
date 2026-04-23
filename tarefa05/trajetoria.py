import telemetria

def main():
    entrada = input()
    v_max = float(input())

    leituras = telemetria.ler_trajetoria(entrada)
    leituras_corrompidas = telemetria.detectar_corrompidas(leituras, v_max)
    trajetoria = telemetria.reconstruir(leituras, leituras_corrompidas)
    
    for t, x, y in trajetoria:
        print(f"{t} {x:.2} {y:.2}")

if __name__ == "__main__":
    main()