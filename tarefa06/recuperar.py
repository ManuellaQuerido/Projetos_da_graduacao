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
    return s[:n//2] == s[n//2:]

nome_vendas = input()
nome_logs = input()

vendas_conhecidas = []
f = open(nome_vendas, "r")
for linha in f:
    if linha[-1] == "\n": linha = linha[:-1]
    if linha: vendas_conhecidas.append(linha.split(","))
f.close()

idx_v = 0
total_acum = 0.0
ultimo_cod = 0
d_ant, c_ant = -1, -1

f = open(nome_logs, "r")
for linha in f:
    if linha[-1] == "\n": linha = linha[:-1]
    if not linha: continue
    
    dados = linha.split(",")
    hora, d_atual, c_atual, t_atual = dados[0], int(dados[1]), int(dados[2]), float(dados[3])

    if t_atual > total_acum + 0.001:
        valor = t_atual - total_acum

        if d_ant != -1:
            cat = "dinossauro" if d_atual < d_ant else "carro"
        else:
 
            if idx_v < len(vendas_conhecidas) and abs(float(vendas_conhecidas[idx_v][3]) - valor) < 0.01:
                cat = vendas_conhecidas[idx_v][2]
            else:
                cat = "dinossauro" if d_atual < c_atual else "carro"

        match = False
        if idx_v < len(vendas_conhecidas):
            v_hora, v_cod, v_cat, v_val = vendas_conhecidas[idx_v]
            if v_hora == hora and abs(float(v_val) - valor) < 0.01 and v_cat == cat:
                ultimo_cod = int(v_cod)
                idx_v += 1
                match = True
        
        if not match:
            cod = ultimo_cod + 1
            while not eh_engracado(cod):
                cod += 1
            print(f"{hora},{cod},{cat},{valor:.2f}")
            ultimo_cod = cod

        total_acum = t_atual
    d_ant, c_ant = d_atual, c_atual
f.close()