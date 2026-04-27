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
        partes = linha.split(",")
        logs.append((partes[0], int(partes[1]), int(partes[2]), float(partes[3])))

# ler vendas
with open(nome_vendas) as arquivo:
    for linha in arquivo:
        partes = linha.split(",")
        vendas.append((partes[0], int(partes[1]), partes[2], float(partes[3])))

# ordenar vendas (simples)
for i in range(len(vendas)):
    for j in range(i+1, len(vendas)):
        if vendas[j][1] < vendas[i][1]:
            temp = vendas[i]
            vendas[i] = vendas[j]
            vendas[j] = temp

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

    if not existe:
        if estoque_dinossauros < estoque_dinossauros_anterior:
            categoria = "dinossauro"
        else:
            categoria = "carro"

        for j in range(len(vendas) - 1):
            codigo1 = vendas[j][1]
            codigo2 = vendas[j+1][1]

            if codigo2 - codigo1 > 1:

                # gerar códigos engraçados pequenos (rápido!)
                for a in range(1, 1000000):
                    s = str(a)
                    codigo = int(s + s)

                    if codigo > codigo1 and codigo < codigo2:
                        print(hora_venda + "," + str(codigo) + "," + categoria + "," + format(valor_da_venda, ".2f"))

    total_anterior = valor_total
    estoque_dinossauros_anterior = estoque_dinossauros
    estoque_carros_anterior = estoque_carros