#ifndef CONFIG_H
#define CONFIG_H

#include <RadioLib.h>
#include "EspHal.h"

#include "radio_config.h"

// ============================================================
// RADIO
// ============================================================

EspHal hal(
    LORA_SCK,
    LORA_MISO,
    LORA_MOSI
);

SX1276 radio = new Module(
    &hal,
    LORA_CS,
    LORA_DIO0,
    LORA_RST,
    LORA_DIO1
);


// ============================================================
// LORAWAN REGION
// ============================================================

// ChirpStack:
// AU915 - channels 0-7 + 64 FSB1
const LoRaWANBand_t Region = AU915;

// AU915 sub-band 1 = channels 0-7 + 64
const uint8_t subBand = 1;


// ============================================================
// OTAA CREDENTIALS
// ============================================================

uint64_t joinEUI = 0xE6EDA694876BD196ULL;

uint64_t devEUI = 0x5ACD739583A4D191ULL;

uint8_t appKey[16] = {
    0x29, 0x19, 0x4D, 0xA8,
    0xA0, 0x2A, 0x1D, 0x7F,
    0xF9, 0x9A, 0x1B, 0xDB,
    0x18, 0x1F, 0x5E, 0xF7
};

uint8_t nwkKey[16] = {
    0x29, 0x19, 0x4D, 0xA8,
    0xA0, 0x2A, 0x1D, 0x7F,
    0xF9, 0x9A, 0x1B, 0xDB,
    0x18, 0x1F, 0x5E, 0xF7
};


// ============================================================
// LORAWAN NODE
// ============================================================

LoRaWANNode node(
    &radio,
    &Region,
    subBand
);


// ============================================================
// UPLINK INTERVAL
// ============================================================

const uint32_t uplinkIntervalSeconds = 300;

#endif