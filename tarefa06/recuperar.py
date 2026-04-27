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
        hora_venda, estoque_dinossauros, estoque_carros, valor_total = linha.strip().split(",")
        logs.append((hora_venda, int(estoque_dinossauros), int(estoque_carros), float(valor_total)))

# ler vendas
with open(nome_vendas) as arquivo:
    for linha in arquivo:
        hora_venda, codigo_vendas, categoria, valor = linha.strip().split(",")
        vendas.append((hora_venda, int(codigo_vendas), categoria, float(valor)))

# ordenar vendas (bubble sort simples)
for i in range(len(vendas)):
    for j in range(i + 1, len(vendas)):
        if vendas[i][1] > vendas[j][1]:
            aux = vendas[i]
            vendas[i] = vendas[j]
            vendas[j] = aux

codigos_engracados = []

for tamanho in [1, 2, 3, 4]:  # controla tamanho (ajustável)
    inicio = 10**(tamanho - 1)
    fim = 10**tamanho

    for i in range(inicio, fim):
        s = str(i)
        codigo = int(s + s)
        codigos_engracados.append(codigo)

# ordenar (garantir ordem)
for i in range(len(codigos_engracados)):
    for j in range(i + 1, len(codigos_engracados)):
        if codigos_engracados[i] > codigos_engracados[j]:
            aux = codigos_engracados[i]
            codigos_engracados[i] = codigos_engracados[j]
            codigos_engracados[j] = aux

total_anterior = logs[0][3]
estoque_dinossauros_anterior = logs[0][1]
estoque_carros_anterior = logs[0][2]

for i in range(1, len(logs)):
    hora_venda = logs[i][0]
    estoque_dinossauros = logs[i][1]
    estoque_carros = logs[i][2]
    valor_total = logs[i][3]

    valor_da_venda = valor_total - total_anterior

    existe = False
    for venda in vendas:
        if venda[0] == hora_venda and venda[3] == valor_da_venda:
            existe = True
            break

    if not existe:

        if estoque_dinossauros < estoque_dinossauros_anterior:
            categoria = "dinossauro"
        else:
            categoria = "carro"

        for j in range(len(vendas) - 1):
            codigo1 = vendas[j][1]
            codigo2 = vendas[j + 1][1]

            if codigo2 - codigo1 > 1:
                for k in codigos_engracados:
                    if codigo1 < k < codigo2:
                        print(f"{hora_venda},{k},{categoria},{valor_da_venda:.2f}")

    total_anterior = valor_total
    estoque_dinossauros_anterior = estoque_dinossauros
    estoque_carros_anterior = estoque_carros