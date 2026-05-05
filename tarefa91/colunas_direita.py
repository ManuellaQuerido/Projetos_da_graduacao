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
                
                if len(novo) <= tamanho:
                    linha_atual = novo
                else:
                    espacos = tamanho - len(linha_atual)
                    linhas_formatadas.append(" " * espacos + linha_atual)
                    linha_atual = palavra
    
    if linha_atual != " ":
        espacos = tamanho - len(linha_atual)
        linhas_formatadas.append(" " * espacos + linha_atual)

i = 0

while i < len(linhas_formatadas):
    pagina = linhas_formatadas[i:i + maximo_linhas]
    i += maximo_linhas

    meio = (len(pagina)+ 1)//2
    coluna_1 = pagina[:meio]
    coluna_2 = pagina[meio:]

    while len(coluna_1) < meio:
        coluna_1.append(" ")
    while len(coluna_2) < meio:
        coluna_2.append(" ")

    for j in range(meio):
        esquerda = coluna_1[j]
        direita = coluna_2[j]

        espacos = maximo_caracteres - len(esquerda) - len(direita)
        print(esquerda + " " * espacos + direita)
    
    print("\n---//---\n")