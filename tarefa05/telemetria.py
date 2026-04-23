import math

def ler_trajetoria():
    n = int(input())
    v_max = float(input())
    leituras = []

    for _ in range(n):
        t, x, y = map(float, input().split())
        leituras.append((t, x, y))

    return v_max, leituras


def distancia(x0, y0, x, y):
    return math.sqrt((x - x0)**2 + (y - y0)**2)


def detectar_corrompidas(leituras, v_max):
    n = len(leituras)
    corrompidas = [False] * n
    ultima_valida = 0

    for i in range(1, n - 1):
        t, x, y = leituras[i]
        ta, xa, ya = leituras[ultima_valida]

        d = distancia(xa, ya, x, y)
        dt = t - ta

        if d / dt > v_max:
            corrompidas[i] = True
        else:
            ultima_valida = i

    return corrompidas


def interpolar(xa, ya, ta, xb, yb, tb, t):
    fator = (t - ta) / (tb - ta)

    x = xa + (xb - xa) * fator
    y = ya + (yb - ya) * fator

    return x, y


def reconstruir(leituras, corrompidas):
    n = len(leituras)
    corrigidas = []

    for i in range(n):
        if not corrompidas[i]:
            corrigidas.append(leituras[i])
        else:
            # acha anterior válida
            j = i - 1
            while corrompidas[j]:
                j -= 1

            # acha posterior válida
            k = i + 1
            while corrompidas[k]:
                k += 1

            ta, xa, ya = leituras[j]
            tb, xb, yb = leituras[k]
            t = leituras[i][0]

            x, y = interpolar(xa, ya, ta, xb, yb, tb, t)
            corrigidas.append((t, x, y))

    return corrigidas


def max_variacao(valores):
    max_v = 0.0

    for i in range(len(valores) - 1):
        variacao = abs(valores[i+1] - valores[i])

        if variacao > max_v:
            max_v = variacao

    return max_v