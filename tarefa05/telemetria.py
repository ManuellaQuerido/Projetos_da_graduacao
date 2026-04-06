def ler_trajetoria():
    """
    Lê os dados de telemetria da entrada padrão.
    A entrada contém o número N de leituras, a velocidade máxima V_max
    e N linhas com instante t, coordenada x e coordenada y.
    Devolve a velocidade máxima e uma lista de tuplas (t, x, y).

    Exemplo de uso: v_max, leituras = ler_trajetoria()
    """


def distancia(x1, y1, x2, y2):
    """
    Recebe as coordenadas de dois pontos (x1, y1) e (x2, y2).
    Devolve a distância euclidiana entre eles.

    Exemplo: distancia(0, 0, 3, 4) devolve 5.0.
    """


def detectar_corrompidas(leituras, v_max):
    """
    Recebe uma lista de tuplas (t, x, y) representando as leituras
    de telemetria e a velocidade máxima da sonda.
    Devolve uma lista de booleanos de mesmo tamanho, onde True
    indica que a leitura correspondente é corrompida.
    A primeira e a última leitura são sempre válidas (False).

    Exemplo de uso: corrompidas = detectar_corrompidas(leituras, v_max)
    """


def interpolar(xa, ya, ta, xb, yb, tb, t):
    """
    Recebe as coordenadas e instantes de dois pontos válidos
    (xa, ya) no instante ta e (xb, yb) no instante tb,
    e o instante t de uma leitura corrompida (ta < t < tb).
    Devolve um par x, y com as coordenadas interpoladas.

    Exemplo: interpolar(0, 0, 0, 10, 10, 4, 2) devolve 5.0, 5.0.
    """


def reconstruir(leituras, corrompidas):
    """
    Recebe uma lista de tuplas (t, x, y) representando as leituras
    de telemetria e uma lista de booleanos indicando quais leituras
    são corrompidas.
    Devolve uma nova lista de tuplas (t, x, y) com a trajetória
    corrigida, substituindo leituras corrompidas por valores
    interpolados.

    Exemplo de uso: corrigida = reconstruir(leituras, corrompidas)
    """


def max_variacao(valores):
    """
    Recebe uma lista de números (com pelo menos dois elementos).
    Devolve a maior diferença absoluta entre dois elementos
    consecutivos da lista.

    Exemplo: max_variacao([1.0, 3.0, 2.0, 5.0]) devolve 3.0,
    pois |5.0 - 2.0| = 3.0 é a maior variação consecutiva.
    """
