#include "lora.h"
#include <stdio.h>

void lora_init(void) {
    printf("LoRa inicializado\n");
}

int lora_available(void) {
    return 1;
}

int lora_receive(char *data, int max_len) {
    snprintf(data, max_len, "pacote_teste");
    return 1;
}

int lora_get_rssi(void) {
    return -60 + (rand() % 10); // Simulação
}