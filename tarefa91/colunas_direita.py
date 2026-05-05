nome_arquivo = input()

valores = input().split()
maximo_caracteres = int(valores[0])
maximo_linhas = int(valores [1])

largura = int(input())

linhas_formatadas = []

with open(nome_arquivo) as f:
  linha_atual = ""

  for linha in f:
    if linha == "\n": #fim do parágrafo 
        if linha_atual != " ":
            espacos = tamanho - len(linha_atual)
            linhas_formatadas.append(" " * espacos + linha_atual)
            linha_atual = " "
            linhas_formatadas.append()
        else:
            palavras = linha.split()
            for palavra in palavras:
                if linha_atual == " ":
                    novo = palavra
                else:
                    novo = linha_atual + " " + palavra