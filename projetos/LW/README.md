# ESP32 LoRaWAN OTAA

Projeto desenvolvido para comunicação LoRaWAN utilizando uma placa ESP32 LoRa (Heltec WiFi LoRa 32 V2) conectando-se a um gateway através do protocolo OTAA.

## Características

- ESP-IDF 5.5
- LoRaWAN OTAA
- Gateway ChirpStack
- Frequência US915
- SX1276
- RadioLib
- LittleFS

## Hardware

- Heltec WiFi LoRa 32 V2
- Gateway Altus GW700

## Estrutura

```
main/
components/
managed_components/
```

## Compilação

```bash
idf.py set-target esp32
idf.py build
idf.py flash
idf.py monitor
```

## Requisitos

- ESP-IDF 5.5 ou superior

## Licença

MIT