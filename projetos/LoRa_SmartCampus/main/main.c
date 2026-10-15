#include <stdio.h>
#include "lora.h"
#include "distance.h"
#include "rssi_filter.h"
#include "config.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

void app_main(void) {

    lora_init();

    config_t cfg = load_config();

    char msg[128];

    while (1) {

        if (lora_available()) {

            lora_receive(msg, sizeof(msg));

            int rssi_raw = lora_get_rssi();

            float rssi = filter_rssi((float) rssi_raw);

            float dist = estimate_distance(rssi, cfg.A, cfg.n);

            printf("\nMSG: %s\n", msg);
            printf("RSSI: %.2f\n", rssi);
            printf("Distância estimada: %.2f m\n", dist);
        }
        
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}