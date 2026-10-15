#include "lorawan.h"
#include "config.h"

#include "esp_log.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

static const char *TAG = "LORAWAN";


// ============================================================
// DECODIFICA STATUS DA RADIOLIB
// ============================================================

static const char *stateDecode(int16_t state)
{
    switch(state)
    {
        case RADIOLIB_ERR_NONE:
            return "ERR_NONE";

        case RADIOLIB_ERR_CHIP_NOT_FOUND:
            return "ERR_CHIP_NOT_FOUND";

        case RADIOLIB_ERR_PACKET_TOO_LONG:
            return "ERR_PACKET_TOO_LONG";

        case RADIOLIB_ERR_RX_TIMEOUT:
            return "ERR_RX_TIMEOUT";

        case RADIOLIB_ERR_MIC_MISMATCH:
            return "ERR_MIC_MISMATCH";

        case RADIOLIB_ERR_INVALID_BANDWIDTH:
            return "ERR_INVALID_BANDWIDTH";

        case RADIOLIB_ERR_INVALID_SPREADING_FACTOR:
            return "ERR_INVALID_SPREADING_FACTOR";

        case RADIOLIB_ERR_INVALID_CODING_RATE:
            return "ERR_INVALID_CODING_RATE";

        case RADIOLIB_ERR_INVALID_FREQUENCY:
            return "ERR_INVALID_FREQUENCY";

        case RADIOLIB_ERR_INVALID_OUTPUT_POWER:
            return "ERR_INVALID_OUTPUT_POWER";

        case RADIOLIB_ERR_NETWORK_NOT_JOINED:
            return "ERR_NETWORK_NOT_JOINED";

        case RADIOLIB_ERR_NO_RX_WINDOW:
            return "ERR_NO_RX_WINDOW";

        case RADIOLIB_ERR_UPLINK_UNAVAILABLE:
            return "ERR_UPLINK_UNAVAILABLE";

        case RADIOLIB_ERR_NO_JOIN_ACCEPT:
            return "ERR_NO_JOIN_ACCEPT";

        case RADIOLIB_ERR_JOIN_NONCE_INVALID:
            return "ERR_JOIN_NONCE_INVALID";

        case RADIOLIB_ERR_NONCES_DISCARDED:
            return "ERR_NONCES_DISCARDED";

        case RADIOLIB_ERR_SESSION_DISCARDED:
            return "ERR_SESSION_DISCARDED";

        case RADIOLIB_LORAWAN_SESSION_RESTORED:
            return "LORAWAN_SESSION_RESTORED";

        case RADIOLIB_LORAWAN_NEW_SESSION:
            return "LORAWAN_NEW_SESSION";

        default:
            return "UNKNOWN";
    }
}


// ============================================================
// INICIALIZAÇÃO DO LORAWAN
// ============================================================

void lorawan_start()
{
    int16_t state;

    ESP_LOGI(TAG, "========================================");
    ESP_LOGI(TAG, "Inicializando LoRaWAN");
    ESP_LOGI(TAG, "========================================");

    // --------------------------------------------------------
    // Inicializa o rádio
    // --------------------------------------------------------

    ESP_LOGI(TAG, "Inicializando SX1276...");

    ConfigLoRa_t radioConfig;

    radioConfig.frequency = 915.0;

    state = radio.begin(radioConfig);

    ESP_LOGI(
        TAG,
        "radio.begin() = %d (%s)",
        state,
        stateDecode(state)
    );

    if(state != RADIOLIB_ERR_NONE)
    {
        ESP_LOGE(TAG, "Falha ao inicializar SX1276");

        while(true)
        {
            vTaskDelay(pdMS_TO_TICKS(1000));
        }
    }

    ESP_LOGI(TAG, "SX1276 inicializado com sucesso");


    // --------------------------------------------------------
    // Configura OTAA
    // --------------------------------------------------------

    ESP_LOGI(TAG, "Configurando OTAA...");

    state = node.beginOTAA(
        joinEUI,
        devEUI,
        nwkKey,
        appKey
    );

    ESP_LOGI(
        TAG,
        "node.beginOTAA() = %d (%s)",
        state,
        stateDecode(state)
    );

    if(state != RADIOLIB_ERR_NONE)
    {
        ESP_LOGE(TAG, "Falha ao configurar OTAA");

        while(true)
        {
            vTaskDelay(pdMS_TO_TICKS(1000));
        }
    }

    ESP_LOGI(TAG, "OTAA configurado");


    // --------------------------------------------------------
    // JOIN
    // --------------------------------------------------------

    ESP_LOGI(TAG, "========================================");
    ESP_LOGI(TAG, "Enviando Join Request...");
    ESP_LOGI(TAG, "========================================");

    state = node.activateOTAA();

    ESP_LOGI(
        TAG,
        "node.activateOTAA() = %d (%s)",
        state,
        stateDecode(state)
    );

    if(state == RADIOLIB_LORAWAN_NEW_SESSION)
    {
        ESP_LOGI(TAG, "========================================");
        ESP_LOGI(TAG, "JOIN ACEITO!");
        ESP_LOGI(TAG, "Dispositivo conectado ao ChirpStack");
        ESP_LOGI(TAG, "========================================");
    }
    else if(state == RADIOLIB_LORAWAN_SESSION_RESTORED)
    {
        ESP_LOGI(TAG, "========================================");
        ESP_LOGI(TAG, "SESSAO RESTAURADA!");
        ESP_LOGI(TAG, "========================================");
    }
    else
    {
        ESP_LOGE(
            TAG,
            "JOIN FALHOU: %d (%s)",
            state,
            stateDecode(state)
        );

        while(true)
        {
            vTaskDelay(pdMS_TO_TICKS(5000));
        }
    }


    // --------------------------------------------------------
    // LOOP DE UPLINK
    // --------------------------------------------------------

    while(true)
    {
        uint8_t payload[3];

        payload[0] = 0x01;
        payload[1] = 0x02;
        payload[2] = 0x03;

        ESP_LOGI(TAG, "Enviando uplink...");

        state = node.sendReceive(
            payload,
            sizeof(payload),
            1
        );

        ESP_LOGI(
            TAG,
            "sendReceive() = %d (%s)",
            state,
            stateDecode(state)
        );

        if(state > 0)
        {
            ESP_LOGI(
                TAG,
                "Downlink recebido na janela RX%d",
                state
            );
        }
        else if(state == RADIOLIB_ERR_NONE)
        {
            ESP_LOGI(TAG, "Uplink enviado. Nenhum downlink.");
        }
        else
        {
            ESP_LOGE(
                TAG,
                "Erro no uplink: %d (%s)",
                state,
                stateDecode(state)
            );
        }

        ESP_LOGI(
            TAG,
            "Aguardando %lu segundos...",
            (unsigned long)uplinkIntervalSeconds
        );

        vTaskDelay(
            pdMS_TO_TICKS(
                uplinkIntervalSeconds * 1000UL
            )
        );
    }
}