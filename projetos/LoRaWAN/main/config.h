#ifndef CONFIG_H
#define CONFIG_H

#include <stdint.h>

#include <RadioLib.h>
#include "EspHal.h"


// =====================================================
// SPI - Heltec WiFi LoRa 32 V2
// =====================================================

EspHal hal(
    5,
    19,
    27
);


SX1276 radio = new Module(
    &hal,
    18,
    26,
    14,
    33
);


// =====================================================
// Região LoRaWAN
// =====================================================

const LoRaWANBand_t Region = AU915;

const uint8_t subBand = 1;



// =====================================================
// Intervalo de envio
// =====================================================

const uint32_t uplinkIntervalSeconds = 60;



// =====================================================
// OTAA
// =====================================================


// JoinEUI
uint64_t joinEUI =
0xc79669cd6acb44d5;


// DevEUI
uint64_t devEUI =
0x7b4323b72a313d5d;


// AppKey
uint8_t appKey[16] =
{
    0x8c, 0x09, 0x95, 0x55,
    0x24, 0xef, 0xdc, 0x19,
    0x24, 0x55, 0x85, 0x69,
    0xc7, 0x99, 0x8e, 0xa5
};


// =====================================================
// Chave de rede
// RadioLib nova versão exige NwkKey
// =====================================================

uint8_t nwkKey[16] =
{
    0x8c, 0x09, 0x95, 0x55,
    0x24, 0xef, 0xdc, 0x19,
    0x24, 0x55, 0x85, 0x69,
    0xc7, 0x99, 0x8e, 0xa5
};



// =====================================================
// Nó LoRaWAN
// =====================================================

LoRaWANNode node(
    &radio,
    &Region,
    subBand
);



// =====================================================
// Decodificador de erros
// =====================================================

const char* stateDecode(int16_t state)
{

    switch(state)
    {

        case RADIOLIB_ERR_NONE:
            return "OK";


        case RADIOLIB_ERR_CHIP_NOT_FOUND:
            return "CHIP_NOT_FOUND";


        case RADIOLIB_ERR_INVALID_FREQUENCY:
            return "INVALID_FREQUENCY";


        case RADIOLIB_ERR_NETWORK_NOT_JOINED:
            return "NETWORK_NOT_JOINED";


        case RADIOLIB_ERR_NO_JOIN_ACCEPT:
            return "NO_JOIN_ACCEPT";


        case RADIOLIB_LORAWAN_NEW_SESSION:
            return "NEW_SESSION";


        case RADIOLIB_LORAWAN_SESSION_RESTORED:
            return "SESSION_RESTORED";


        default:
            return "UNKNOWN";
    }

}


#endif