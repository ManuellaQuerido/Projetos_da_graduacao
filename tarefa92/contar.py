"""
Entrada: A matriz da imagem e a posição (linha = i, coluna = j).
Saída: Todos os pixels da região conectada são pintados de branco.

Casos base:
    - posição fora da imagem;
    - pixel branco.

Caso geral: Pinta o pixel atual de branco e reduz o problema para
as quatro regiões vizinhas (cima, baixo, esquerda e direita).
"""


def marcar(imagem, i, j):

    if i < 0 or i >= len(imagem):
        return

    if j < 0 or j >= len(imagem[0]):
        return

    if imagem[i][j] != 0:
        return

    imagem[i][j] = 255

    marcar(imagem, i-1, j)
    marcar(imagem, i+1, j)
    marcar(imagem, i, j-1)
    marcar(imagem, i, j+1)


def main():

    nome_arquivo = input().strip()

    arquivo = open(nome_arquivo, "r")
    linhas = arquivo.readlines()
    arquivo.close()
    
    conteudo = []
    for linha in linhas:
        linha_limpa = linha.strip()
        
        if len(linha_limpa) > 0 and linha_limpa[0] != "#":
            palavras_da_linha = linha_limpa.split()
            
            for palavra in palavras_da_linha:
                conteudo.append(palavra)

    largura = int(conteudo[1])
    altura = int(conteudo[2])
    
    dados_pixels = conteudo[4:]

    pixels_inteiros = []
    for p in dados_pixels:
        pixels_inteiros.append(int(p))

    imagem = []
    for i in range(altura):
        inicio = i * largura
        fim = inicio + largura
        linha_matriz = pixels_inteiros[inicio:fim]
        imagem.append(linha_matriz)

    total_colonias = 0
    for i in range(altura):
        for j in range(largura):
            if imagem[i][j] == 0:
                total_colonias += 1
                marcar(imagem, i, j)

    print(f"A imagem tem {total_colonias} colônias.")


main()