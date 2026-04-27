# 1.Ler arquivo vendas.csv e logs.csv

# 2.Para cada log a partir da segunda linha:
    # O valor total acumulado das vendas é a diferença entre 
    # o valor total atual e o valor total anterior computados

# 3.Em vendas.csv, existe uma venda com mesma hora e valor?
    # Se for verdadeiro:
        # a venda não foi deletadas
    # Senão:
        # a venda foi deletada

    # Se o estoque_dinossauro diminuiu
        # Então, a categoria é dinossauro
    # Se o estoque_carros diminuiu
        # Então, a categoria é carro

    # Percorrer a lista de vendas
        # Diferença entre os códigos consecutivos (codigo1 e codigo2)
        # Para cada par em (codigo1, codigo2)
            # Se a diferença for maior que 1
                # Para cada par de códigos
                    # Se o código for engraçado
                        # CÓDIGO DELETADO ENCONTRADO
                    # Parar a busca
                    # Se o código não for enrgraçado
                        # VENDA NÃO DELETADA

# 4.Imprimir "hora, código, categoria, valor"
vendas = []
logs = []

nome_vendas = input()
nome_logs = input()

# ler logs
with open(nome_logs) as arquivo:
    for linha in arquivo:
        # substitui o strip() manual retirando a quebra de linha
        if linha[-1] == "\n":
            linha = linha[:-1]
            
        partes = linha.split(",")
        logs.append((partes[0], int(partes[1]), int(partes[2]), float(partes[3])))

# ler vendas
with open(nome_vendas) as arquivo:
    for linha in arquivo:
        if linha[-1] == "\n":
            linha = linha[:-1]
            
        partes = linha.split(",")
        vendas.append((partes[0], int(partes[1]), partes[2], float(partes[3])))

# 🚀 OTIMIZAÇÃO 1: Ordenação rápida e permitida para iniciantes
# O Python já sabe ordenar listas de tuplas pelo primeiro elemento numérico.
# Como o código está na posição [1], guardamos (codigo, hora, categoria, valor)
vendas_ordenadas = []
for v in vendas:
    vendas_ordenadas.append((v[1], v[0], v[2], v[3]))

# O comando .sort() não usa lambda e é extremamente rápido!
vendas_ordenadas.sort()

# Guardando apenas os códigos existentes para busca rápida
codigos_existentes = set()
for v in vendas:
    codigos_existentes.add(v[1])

total_anterior = logs[0][3]
estoque_dinossauros_anterior = logs[0][1]

for i in range(1, len(logs)):
    hora_venda = logs[i][0]
    estoque_dinossauros = logs[i][1]
    valor_total = logs[i][3]

    valor_da_venda = valor_total - total_anterior

    # 🚀 OTIMIZAÇÃO 2: Procurando a venda de forma rápida
    existe = False
    for v in vendas:
        if v[0] == hora_venda and v[3] == valor_da_venda:
            existe = True
            break # se achou, não precisa continuar procurando!

    if not existe:
        if estoque_dinossauros < estoque_dinossauros_anterior:
            categoria = "dinossauro"
        else:
            categoria = "carro"

        # Procurando o código pulado
        for j in range(len(vendas_ordenadas) - 1):
            codigo1 = vendas_ordenadas[j][0]
            codigo2 = vendas_ordenadas[j+1][0]

            if codigo2 - codigo1 > 1:
                
                # 🚀 OTIMIZAÇÃO 3: Gerando códigos engraçados inteligentes
                # Em vez de 1 milhão, gera apenas no tamanho do código anterior
                tamanho = len(str(codigo1)) // 2
                if tamanho == 0:
                    tamanho = 1
                
                encontrou = False
                for t in range(tamanho, tamanho + 3):
                    inicio = 10**(t-1)
                    fim = 10**t
                    
                    for num in range(inicio, fim):
                        s = str(num)
                        codigo_engracado = int(s + s)
                        
                        if codigo1 < codigo_engracado and codigo_engracado < codigo2:
                            # garante que o código realmente sumiu
                            if codigo_engracado not in codigos_existentes:
                                print(hora_venda + "," + str(codigo_engracado) + "," + categoria + "," + format(valor_da_venda, ".2f"))
                                encontrou = True
                                break
                    if encontrou:
                        break
                if encontrou:
                    break

    total_anterior = valor_total
    estoque_dinossauros_anterior = estoque_dinossauros