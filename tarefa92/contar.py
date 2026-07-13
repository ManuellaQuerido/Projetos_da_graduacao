def marcar(imagem, linha, coluna):
    """
    Entrada:
        A matriz da imagem e a posição (linha, coluna).

    Saída:
        Todos os pixels da região conectada são pintados de branco.

    Casos básicos:
        - posição fora da imagem;
        - pixel branco.

    Caso geral:
        Pinta o pixel atual de branco e reduz o problema para
        as quatro regiões vizinhas (cima, baixo, esquerda e direita).
    """
