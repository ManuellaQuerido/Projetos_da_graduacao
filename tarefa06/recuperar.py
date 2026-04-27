# Ler arquivo vendas.csv e logs.csv

# Para cada log a partir da segunda linha:
    # O valor total acumulado das vendas é a diferença entre 
    # o valor total atual e o valor total anterior computados

# Em vendas.csv, existe uma venda com mesma hora e valor?
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

# Imprimir "hora, código, categoria, valor"

vendas = []
logs = []

nome_vendas = input()
nome_logs = input()

#ler arquivos logs e vendas
with open(nome_logs) as arquivo:
    for linha in arquivo:
        hora_venda,estoque_dinossauros,estoque_carros,valor_total = linha.split(",")
        logs.append(hora_venda, int(estoque_dinossauros), int(estoque_carros), float(valor_total))

with open("dados/vendas.csv") as arquivo:
    for linha in arquivo:
        hora_venda,código_vendas,categoria,valor = linha.split(",")
        vendas = (hora, int(código_vendas), categoria, float(valor))