#ifndef LORA_H
#define LORA_H

void lora_init(void);
int lora_receive(char *data, int max_len);
int lora_available(void);
int lora_get_rssi(void);

#endif