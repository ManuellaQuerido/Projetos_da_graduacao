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
    for tam in range(1, n // 2 + 1):
        for i in range(n - 2 * tam + 1):
            sub = s[i : i + tam]
            proxima = s[i + tam : i + 2 * tam]
            if sub == proxima:
                return True
    return False


nome_vendas = input()
nome_logs = input()

vendas_conhecidas = []
f_v = open(nome_vendas, "r")
for linha in f_v:
    if linha[-1] == "\n":
        linha = linha[:-1]
    vendas_conhecidas.append(linha.split(","))
f_v.close()

idx_v = 0
total_acumulado = 0.0
ultimo_cod = 0
est_dino_ant = -1
est_carro_ant = -1

f_l = open(nome_logs, "r")
for linha in f_l:
    if linha[-1] == "\n":
        linha = linha[:-1]
    
    dados = linha.split(",")
    hora_log = dados[0]
    est_dino = int(dados[1])
    est_carro = int(dados[2])
    total_log = float(dados[3])

    if total_log > total_acumulado:
        valor_venda = total_log - total_acumulado

        if idx_v < len(vendas_conhecidas) and vendas_conhecidas[idx_v][0] == hora_log:
            ultimo_cod = int(vendas_conhecidas[idx_v][1])
            idx_v += 1
        else:
            if est_dino_ant != -1 and est_dino < est_dino_ant:
                categoria = "dinossauro"
            else:
                categoria = "carro"

            limite_sup = 2147483647
            if idx_v < len(vendas_conhecidas):
                limite_sup = int(vendas_conhecidas[idx_v][1])

            cod_rec = ultimo_cod + 1

            while cod_rec < limite_sup:
                if eh_engracado(cod_rec):
                    break
                cod_rec = cod_rec + 1

            print(hora_log + "," + str(cod_rec) + "," + categoria + "," + "{:.2f}".format(valor_venda))
            ultimo_cod = cod_rec

        total_acumulado = total_log

    est_dino_ant = est_dino
    est_carro_ant = est_carro

f_l.close()