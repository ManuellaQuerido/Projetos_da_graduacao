#ifndef CONFIG_H
#define CONFIG_H

typedef struct {
    float A;
    float n;
} config_t;

config_t load_config(void);

#endif