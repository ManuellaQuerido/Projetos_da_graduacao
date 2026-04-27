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
    # Tenta encontrar qualquer repetição consecutiva
    for tam in range(1, n // 2 + 1):
        for i in range(n - 2 * tam + 1):
            sub = s[i : i + tam]
            proxima = s[i + tam : i + 2 * tam]
            if sub == proxima:
                return True
    return False

# Nomes dos arquivos
nome_vendas = input()
nome_logs = input()

# Lendo vendas existentes
vendas_existentes = []
arquivo_v = open(nome_vendas, "r")
for linha in arquivo_v:
    # Removendo o \n manualmente se ele existir
    if linha[-1] == "\n":
        linha = linha[:-1]
    vendas_existentes.append(linha.split(","))
arquivo_v.close()

total_vendas_conhecidas = 0.0
idx_v = 0
ultimo_codigo = 0
estoque_dino_ant = -1
estoque_carro_ant = -1

arquivo_l = open(nome_logs, "r")
for linha in arquivo_l:
    if linha[-1] == "\n":
        linha = linha[:-1]
    
    dados_log = linha.split(",")
    hora_log = dados_log[0]
    est_dino = int(dados_log[1])
    est_carro = int(dados_log[2])
    total_log = float(dados_log[3])

    # Verifica se a venda do log é uma que já temos no arquivo de vendas
    venda_ja_existe = False
    if idx_v < len(vendas_existentes):
        if vendas_existentes[idx_v][0] == hora_log:
            venda_ja_existe = True
    
    if venda_ja_existe:
        total_vendas_conhecidas += float(vendas_existentes[idx_v][3])
        ultimo_codigo = int(vendas_existentes[idx_v][1])
        idx_v += 1
    else:
        # Se não existe, Tim deletou! Precisamos recuperar.
        valor_deletado = total_log - total_vendas_conhecidas
        
        # Descobre a categoria vendo qual estoque diminuiu
        categoria = ""
        if est_dino < estoque_dino_ant:
            categoria = "dinossauro"
        else:
            categoria = "carro"
            
        # Define o limite para busca do código
        limite_superior = 2000000000 # Um número bem grande
        if idx_v < len(vendas_existentes):
            limite_superior = int(vendas_existentes[idx_v][1])
            
        # Busca o código engraçado
        codigo_recuperado = 0
        for c in range(ultimo_codigo + 1, limite_superior):
            if eh_engracado(c):
                codigo_recuperado = c
                break
        
        print(f"{hora_log},{codigo_recuperado},{categoria},{valor_deletado:.2f}")
        
        # Atualiza o total e o último código para a próxima volta
        total_vendas_conhecidas = total_log
        ultimo_codigo = codigo_recuperado

    # Guarda os estoques para comparar na próxima linha
    estoque_dino_ant = est_dino
    estoque_carro_ant = est_carro

arquivo_l.close()