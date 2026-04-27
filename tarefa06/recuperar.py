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
def eh_engracado(codigo):
    s = str(codigo)
    n = len(s)
    if n % 2 != 0: return False
    metade = n // 2
    return s[:metade] == s[metade:]

nome_vendas = input()
nome_logs = input()

vendas_conhecidas = []
f = open(nome_vendas, "r")
for linha in f:
    if linha[-1] == "\n": linha = linha[:-1]
    if linha: vendas_conhecidas.append(linha.split(","))
f.close()

idx_v = 0
total_acumulado = 0.0
ultimo_cod = 0
est_dino_ant = -1

f = open(nome_logs, "r")
for linha in f:
    if linha[-1] == "\n": linha = linha[:-1]
    if not linha: continue
    
    dados = linha.split(",")
    hora_log, est_dino, total_log = dados[0], int(dados[1]), float(dados[3])

    if total_log > total_acumulado + 0.001:
        valor_venda = total_log - total_acumulado
        
        # Procura o próximo número engraçado possível
        prox_engracado = ultimo_cod + 1
        while not eh_engracado(prox_engracado):
            prox_engracado += 1
            
        eh_deletada = True
        # Se existe uma venda conhecida e o código dela é MENOR que o próximo engraçado,
        # significa que a venda atual do log É a venda conhecida.
        if idx_v < len(vendas_conhecidas):
            cod_conhecida = int(vendas_conhecidas[idx_v][1])
            if cod_conhecida < prox_engracado:
                ultimo_cod = cod_conhecida
                idx_v += 1
                eh_deletada = False
        
        if eh_deletada:
            categoria = "dinossauro" if (est_dino_ant != -1 and est_dino < est_dino_ant) else "carro"
            print(hora_log + "," + str(prox_engracado) + "," + categoria + "," + "{:.2f}".format(valor_venda))
            ultimo_cod = prox_engracado
            
        total_acumulado = total_log
    est_dino_ant = est_dino
f.close()