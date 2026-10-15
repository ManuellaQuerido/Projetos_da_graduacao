#include <math.h>
#include "distance.h"

float estimate_distance(float rssi, float A, float n) {
    return pow(10, (A - rssi) / (10 * n));
}