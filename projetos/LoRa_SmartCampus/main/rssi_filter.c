#include "rssi_filter.h"

float filter_rssi(float rssi) {
    static float prev = -50;
    float alpha = 0.2;

    prev = alpha * rssi + (1 - alpha) * prev;
    return prev;
}