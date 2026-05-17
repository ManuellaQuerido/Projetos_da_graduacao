def ler_pgm(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        tipo = arquivo.readline().strip()

        linha = arquivo.readline().strip()
        while linha.startswith("#"):
            linha = arquivo.readline().strip()

        largura, altura = map(int, linha.split())
        maximo = int(arquivo.readline().strip())

        pixels = []
