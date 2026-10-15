#include "config.h"
#include <stdio.h>

// versão simples (depois você pode ler JSON real)
config_t load_config(void) {
    config_t cfg;

    cfg.A = -40;
    cfg.n = 2.2;

    printf("Config carregada\n");

    return cfg;
}