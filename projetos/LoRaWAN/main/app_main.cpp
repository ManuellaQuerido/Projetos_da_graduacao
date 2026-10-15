#include <stdio.h>

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#include "esp_log.h"

#include "config.h"

static const char *TAG = "LORAWAN";

extern "C" void app_main()
{
    // =====================================================
    // 1) Inicializa o rádio (SX1276)
    // =====================================================

    ESP_LOGI(TAG, "Inicializando rádio...");

    int16_t state = radio.begin(915.0);

    if(state != RADIOLIB_ERR_NONE)
    {
        ESP_LOGE(TAG,
                 "Erro ao iniciar rádio: %s (%d)",
                 stateDecode(state),
                 state);

        while(true)
        {
            vTaskDelay(pdMS_TO_TICKS(1000));
        }
    }

    ESP_LOGI(TAG, "Rádio iniciado!");

    // =====================================================
    // 2) Configura a sessão OTAA (ainda não transmite nada)
    // =====================================================

    ESP_LOGI(TAG, "Configurando sessão OTAA...");

    state = node.beginOTAA(joinEUI, devEUI, nwkKey, appKey);

    if(state != RADIOLIB_ERR_NONE)
    {
        ESP_LOGE(TAG,
                 "Erro ao configurar OTAA: %s (%d)",
                 stateDecode(state),
                 state);

        while(true)
        {
            vTaskDelay(pdMS_TO_TICKS(1000));
        }
    }

    ESP_LOGI(TAG, "OTAA configurada!");

    // =====================================================
    // 3) Envia o Join Request e aguarda o Join Accept
    //    Aqui é onde o erro NO_JOIN_ACCEPT aparecia antes
    // =====================================================

    ESP_LOGI(TAG, "Enviando Join Request...");

    state = node.activateOTAA();

    // RADIOLIB_LORAWAN_NEW_SESSION = join bem-sucedido, sessão nova
    // RADIOLIB_LORAWAN_SESSION_RESTORED = sessão salva foi restaurada

    if(state != RADIOLIB_LORAWAN_NEW_SESSION &&
       state != RADIOLIB_LORAWAN_SESSION_RESTORED)
    {
        ESP_LOGE(TAG,
                 "Join falhou: %s (%d)",
                 stateDecode(state),
                 state);

        ESP_LOGE(TAG,
                 "Verifique: sub-band do gateway, region config no "
                 "ChirpStack (au915_0), DevEUI, JoinEUI e AppKey.");

        while(true)
        {
            vTaskDelay(pdMS_TO_TICKS(1000));
        }
    }

    ESP_LOGI(TAG, "Join aceito! Dispositivo conectado à rede LoRaWAN.");

    // =====================================================
    // 4) Loop de uplinks
    // =====================================================

    uint32_t counter = 0;

    while(true)
    {
        // Payload de teste: só um contador de 1 byte.
        // Depois trocamos por dados reais (ex: distância via RSSI).
        uint8_t uplinkPayload[1];
        uplinkPayload[0] = (uint8_t)(counter & 0xFF);

        ESP_LOGI(TAG, "Enviando uplink #%lu...", (unsigned long)counter);

        state = node.sendReceive(uplinkPayload, sizeof(uplinkPayload));

        if(state < RADIOLIB_ERR_NONE)
        {
            ESP_LOGE(TAG,
                     "Erro ao enviar uplink: %s (%d)",
                     stateDecode(state),
                     state);
        }
        else
        {
            ESP_LOGI(TAG, "Uplink enviado!");

            // state > 0 significa que veio downlink junto
            if(state > 0)
            {
                ESP_LOGI(TAG, "Downlink recebido (%d bytes de payload de downlink pendente)", state);
            }
        }

        counter++;

        vTaskDelay(pdMS_TO_TICKS(uplinkIntervalSeconds * 1000UL));
    }
}