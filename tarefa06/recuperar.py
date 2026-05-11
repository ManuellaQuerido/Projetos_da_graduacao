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
                    # Se o código não for engraçado
                        # VENDA NÃO DELETADA

# 4.Imprimir "hora, código, categoria, valor"


def engraçado(codigo):
    s = str(codigo)
    if len(s) % 2 != 0:
        return False
    
    metade = len(s) // 2

    if s[:metade] == s[metade:]:
        return True

    return False


def carregar_vendas(arquivo):
    vendas = []
    with open(arquivo) as pasta:
        for linha in pasta:
            if linha[-1] == "\n":
                linha = linha[:-1]
            dados = linha.split(",")
            vendas.append(dados)
    
    return vendas


def procurar_codigo(codigo):
    while engraçado(codigo) == False:
        codigo += 1
    return codigo


def main():
    nome_vendas = input()
    nome_logs = input()

    vendas = carregar_vendas(nome_vendas)
    indice = 0
    total_anterior = 0
    codigo_anterior = 0
    estoque_carro_anterior = -1
    estoque_dinossauro_anterior = -1

    with open(nome_logs) as pasta:
        for linha in pasta:
            if linha[-1] == "\n":
                linha = linha[:-1]

            dados = linha.split(",")
            hora = dados[0]

            estoque_dinossauro = int(dados[1])
            estoque_carros = int(dados[2])

            total = float(dados[3])

            if total > total_anterior:
                valor = total - total_anterior

                if estoque_dinossauro_anterior != -1:
                    if estoque_dinossauro < estoque_dinossauro_anterior:
                        categoria = "dinossauro"
                    
                    else:
                        categoria = "carro"
                
                else:
                    if indice < len(vendas):
                        categoria = vendas[indice][2]
                    else:
                        if estoque_dinossauro < estoque_carros:
                            categoria = "dinossauro"
                        else:
                            categoria = "carro"
                
                encontrou = False

                if indice < len(vendas):
                    venda = vendas[indice]
                    hora_venda = venda[0]
                    codigo_venda = venda[1]
                    categoria_venda = venda[2]
                    valor_venda = float(venda[3])

                    if hora == hora_venda:
                        if categoria == categoria_venda:
                            if valor == valor_venda:
                                codigo_anterior = int(codigo_venda)
                                indice += 1
                                encontrou = True
                
                if encontrou == False:
                    codigo = codigo_anterior + 1
                    codigo = procurar_codigo(codigo)
                    print(f"{hora},{codigo},{categoria},{valor:.2f}")
                    codigo_anterior = codigo
                
                total_anterior = total
            
            estoque_dinossauro_anterior = estoque_dinossauro
            estoque_carro_anterior = estoque_carros

main()