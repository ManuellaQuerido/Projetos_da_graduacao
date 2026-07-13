def contar_disco(imagem): #função adicionada

    pretos = 0

    if imagem[indice] == 0:
        pretos += 1

    return pretos

def main():
    entrada = input()
    arquivo = open(entrada, "r")
    linhas = []
    for linha in arquivo:
        linhas.append(linha)
    
    # conta pretos dentro do disco

    pixels_pretos = contar_disco(imagem)

    # estima colônias
    colonias = pixels_pretos // media

    resultado = colonias
    print(f"A imagem tem {resultado} colônias")

main()