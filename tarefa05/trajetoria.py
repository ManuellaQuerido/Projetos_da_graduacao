import telemetria.py

def main():
    Vmax, leituras = telemetria.ler_trajetoria()
    corrompidas = telemetria.detectar_corrompidas(leituras)
    distancia = telemetria.distancia()
