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

# Ler logs
with open(nome_logs) as arquivo:
    for linha in arquivo:
        hora_venda, estoque_dinossauros, estoque_carros, valor_total = linha.strip().split(",")
        logs.append((hora_venda, int(estoque_dinossauros), int(estoque_carros), float(valor_total)))

# Ler vendas
with open(nome_vendas) as arquivo:
    for linha in arquivo:
        hora_venda, código_vendas, categoria, valor = linha.strip().split(",")
        vendas.append((hora_venda, int(código_vendas), categoria, float(valor)))

# Variáveis iniciais
total_anterior = logs[0][3]
estoque_dinossauros_anterior = logs[0][1]
estoque_carros_anterior = logs[0][2]

# Percorrer logs
for i in range(1, len(logs)):
    hora_venda = logs[i][0]
    estoque_dinossauros = logs[i][1]
    estoque_carros = logs[i][2]
    valor_total = logs[i][3]

    valor_da_venda = valor_total - total_anterior

    # Verificar se existe
    existe = False
    for venda in vendas:
        if venda[0] == hora_venda and venda[3] == valor_da_venda:
            existe = True
            break

    # Se não existe, encontrar categoria
    if not existe:

        if estoque_dinossauros < estoque_dinossauros_anterior:
            categoria = "dinossauro"
        else:
            categoria = "carro"

        codigo_encontrado = 0

        # Procurar código faltando
        for j in range(len(vendas) - 1):
            código1 = vendas[j][1]
            código2 = vendas[j+1][1]

            if código2 - código1 > 1:
                for k in range(código1 + 1, código2):
                    s = str(k)

                    if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
                        codigo_encontrado = k
                        break

            if codigo_encontrado != 0:
                break

        print(f"{hora_venda},{codigo_encontrado},{categoria},{valor_da_venda:.2f}")

        vendas.append((hora_venda, codigo_encontrado, categoria, valor_da_venda))
            for m in range(len(vendas)):
                for n in range(m + 1, len(vendas)):
                    if vendas[m][1] > vendas[n][1]:
                        vendas[], vendas[n] = vendas[n], vendas[a]

    # Atualizar valores
    total_anterior = valor_total
    estoque_dinossauros_anterior = estoque_dinossauros
    estoque_carros_anterior = estoque_carros