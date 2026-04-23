import math

def ler_trajetoria(x0, y0, x, y):
# Lê os dados de telemetria da entrada padrão. A entrada contém o número N de leituras, a velocidade máxima V_max e N linhas com instante t, coordenada x e coordenada y. Devolve a velocidade máxima e uma lista de tuplas (t, x, y). Exemplo de uso: v_max, leituras = ler_trajetoria()

    n = int(input())
    vmax = float(input())
    leituras = []

    for i in range(n):
        dados = input().split()
        t = float(dados[0])
        x = float(dados[1])
        y = float(dados[2])

        leituras.append((t, x, y))

    return vmax, leituras


def distancia(x0, y0, x, y):
#    Recebe as coordenadas de dois pontos (x0, y0) e (x, y). Devolve a distância euclidiana entre eles. Exemplo: distancia(0, 0, 3, 4) devolve 5.0.

    d = math.sqrt((x - x0)**2 + (y - y0)**2)
    
    return d


def detectar_corrompidas(leituras, v_max):
#    Recebe uma lista de tuplas (t, x, y) representando as leituras de telemetria e a velocidade máxima da sonda. Devolve uma lista de booleanos de mesmo tamanho, onde True indica que a leitura correspondente é corrompida. A primeira e a última leitura são sempre válidas (False). Exemplo de uso: corrompidas = detectar_corrompidas(leituras, v_max)

    n = len(leituras) 
    leituras_corrompidas = []
    ultima_valida = 0

    for i in range(n):
        leituras_corrompidas.append(False)

    for i in range(1, n - 1):
        t_atual, x_atual, y_atual = leituras[i]
        t_anterior, x_anterior, y_anterior = leituras[ultima_valida]

        d = distancia(x_anterior, y_anterior, x_atual, y_atual)

        T = t_atual - t_anterior # T = delta t

        if d / T > vmax:
            leituras_corrompidas[i] = True
        else:
            ultima_valida = i

    return leituras_corrompidas


def interpolar(xa, ya, ta, xb, yb, tb, t):
# Recebe as coordenadas e instantes de dois pontos válidos (xa, ya) no instante ta e (xb, yb) no instante tb, e o instante t de uma leitura corrompida (ta < t < tb). Devolve um par x, y com as coordenadas interpoladas. Exemplo: interpolar(0, 0, 0, 10, 10, 4, 2) devolve 5.0, 5.0.

    instantes = (t - ta) / (tb - ta)

    x = xa + (xb - xa) * instantes
    y = ya + (yb - ya) * instantes

    return x, y


def reconstruir(leituras, corrompidas):
#    Recebe uma lista de tuplas (t, x, y) representando as leituras de telemetria e uma lista de booleanos indicando quais leituras são corrompidas. Devolve uma nova lista de tuplas (t, x, y) com a trajetória corrigida, substituindo leituras corrompidas por valores interpolados. Exemplo de uso: corrigida = reconstruir(leituras, corrompidas)

    leituras_corrigidas = []
    n = len(leituras)

    for i in range(n):
        if not leituras_corrompidas[i]:
            leituras_corrigidas.append(leituras[i])
        else:
            posição_anterior = i - 1
            while leituras_corrompidas[posição_anterior] == True:
                posições_anterior -= 1

            posição_posterior = i + 1
            while leituras_corrompidas[posição_posterior] == True:
                posição_posterior += 1
            
            ta, xa, ya = leituras[posição_anterior]
            tb, xb, yb = leituras[posição_posterior]
            t_atual = leituras[i][0]
            
            x_novo, y_novo = interpolar(xa, ya, ta, xb, yb, tb, t_atual)

            leituras_corrigidas.append((t_atual, x_novo, y_novo))

    return leituras_corrigidas


def max_variacao(valores):
    #"Recebe uma lista de números (com pelo menos dois elementos). Devolve a maior diferença absoluta entre dois elementos consecutivos da lista. Exemplo: max_variacao([1.0, 3.0, 2.0, 5.0]) devolve 3.0, pois |5.0 - 2.0| = 3.0 é a maior variação consecutiva."

    max_v = 0.0

    for i in range(len(valores) - 1):
        v_atual = valores[i]
        v_proximo = valores[i + 1]

        variação = v_proximo - v_atual
        if variação < 0:
            variação = -variação
        elif variação < max_v:
            max_v = variação

    return max_v
