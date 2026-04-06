import telemetria.py

Vmax, leituras = telemetria.ler_trajetoria()
corrompidas = telemetria.detectar_corrompidas(leituras)
distancia = telemetria.distancia()
