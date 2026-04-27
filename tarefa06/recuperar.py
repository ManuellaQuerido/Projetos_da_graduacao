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

# 1. Ler logs
with open(nome_logs) as arquivo:
    for linha in arquivo:
        if linha[-1] == "\n":
            linha = linha[:-1]
            
        partes = linha.split(",")
        logs.append((partes[0], int(partes[1]), int(partes[2]), float(partes[3])))

# 2. Ler vendas
with open(nome_vendas) as arquivo:
    for linha in arquivo:
        if linha[-1] == "\n":
            linha = linha[:-1]
            
        partes = linha.split(",")
        vendas.append((partes[0], int(partes[1]), partes[2], float(partes[3])))

# Guardar os códigos existentes para busca rápida
codigos_existentes = set()
for v in vendas:
    codigos_existentes.add(v[1])

# OTIMIZAÇÃO: Ordenar as vendas originais usando o próprio .sort() do Python
vendas_ordenadas = []
for v in vendas:
    vendas_ordenadas.append((v[1], v[0], v[2], v[3])) # Código em primeiro para ordenar por ele
vendas_ordenadas.sort()

total_anterior = logs[0][3]
estoque_dinossauros_anterior = logs[0][1]

# 3. Processar logs
for i in range(1, len(logs)):
    hora_venda = logs[i][0]
    estoque_dinossauros = logs[i][1]
    valor_total = logs[i][3]

    valor_da_venda = valor_total - total_anterior

    # Verificar se a venda existe
    existe = False
    for v in vendas:
        if v[0] == hora_venda and v[3] == valor_da_venda:
            existe = True
            break

    # Se a venda não existe, ela foi deletada!
    if not existe:
        if estoque_dinossauros < estoque_dinossauros_anterior:
            categoria = "dinossauro"
        else:
            categoria = "carro"

        codigo_engracado_encontrado = None

        # Vamos procurar qual código sumiu olhando os buracos da lista ordenada
        for j in range(len(vendas_ordenadas) - 1):
            codigo1 = vendas_ordenadas[j][0]
            codigo2 = vendas_ordenadas[j+1][0]

            # Se houver um buraco maior que 1 entre os códigos
            if codigo2 - codigo1 > 1:
                
                # Gerador focado no tamanho dos códigos que estão faltando!
                tam_codigo = len(str(codigo1))
                tam_metade = tam_codigo // 2
                
                # Se for código pequeno (ex: de 1 a 99)
                if tam_metade == 0:
                    tam_metade = 1
                
                # Tentamos gerar códigos espelhados do tamanho certo
                inicio = 10**(tam_metade - 1)
                fim = 10**tam_metade
                
                for num in range(inicio, fim):
                    s = str(num)
                    codigo_engracado = int(s + s)
                    
                    # Se o código cair dentro do buraco e não existir, achamos!
                    if codigo1 < codigo_engracado and codigo_engracado < codigo2:
                        if codigo_engracado not in codigos_existentes:
                            codigo_engracado_encontrado = codigo_engracado
                            break
                
                if codigo_engracado_encontrado is not None:
                    break
        
        # Caso especial (teste 6): Se o buraco for antes da primeira venda
        if codigo_engracado_encontrado is None and len(vendas_ordenadas) > 0:
            primeiro_codigo = vendas_ordenadas[0][0]
            num = 1
            while True:
                s = str(num)
                codigo_engracado = int(s + s)
                if codigo_engracado >= primeiro_codigo:
                    break
                if codigo_engracado not in codigos_existentes:
                    codigo_engracado_encontrado = codigo_engracado
                    break
                num += 1

        print(hora_venda + "," + str(codigo_engracado_encontrado) + "," + categoria + "," + format(valor_da_venda, ".2f"))
        codigos_existentes.add(codigo_engracado_encontrado)

    total_anterior = valor_total
    estoque_dinossauros_anterior = estoque_dinossauros

