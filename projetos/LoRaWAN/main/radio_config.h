#ifndef RADIO_CONFIG_H
#define RADIO_CONFIG_H

#include <RadioLib.h>
#include "EspHal.h"

// SPI
#define LORA_SCK   5
#define LORA_MISO 19
#define LORA_MOSI 27

// SX1276
#define LORA_CS    18
#define LORA_DIO0  26
#define LORA_RST   14
#define LORA_DIO1  35

extern EspHal* hal;
extern SX1276 radio;

#endif
