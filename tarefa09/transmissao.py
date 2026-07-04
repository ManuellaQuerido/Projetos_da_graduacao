def main():
    k = int(input())
    estilos_exigidos = set(input().split())
    
    n = int(input())
    shows = []
    
    # Ler os shows
    for _ in range(n):
        linha = input().split()
        nome = linha[0]
        estilo = linha[1]
        shows.append((nome, estilo))
    
    # Técnica: Janela Deslizante (Sliding Window)
    esquerda = 0
    estilo_count = {}  # Dicionário contando shows de cada estilo na janela
    estilos_presentes = 0  # Quantos estilos diferentes já temos
    
    melhor_inicio = 0
    melhor_fim = n
    melhor_tamanho = n + 1
    
    # Expandir a janela pela direita
    for direita in range(n):
        nome_d, estilo_d = shows[direita]
        
        # Adicionar show à direita da janela
        if estilo_d in estilos_exigidos:
            if estilo_d not in estilo_count:
                estilo_count[estilo_d] = 0
            
            # Se é a primeira vez que vemos este estilo, incrementar contador
            if estilo_count[estilo_d] == 0:
                estilos_presentes += 1
            
            estilo_count[estilo_d] += 1
        
        # Tentar encolher pela esquerda mantendo validez
        while estilos_presentes == len(estilos_exigidos):
            # Janela atual é válida (tem todos os estilos)
            tamanho = direita - esquerda + 1
            
            # Atualizar melhor se este é menor
            if tamanho < melhor_tamanho:
                melhor_tamanho = tamanho
                melhor_inicio = esquerda
                melhor_fim = direita + 1
            
            # Remover show da esquerda
            nome_e, estilo_e = shows[esquerda]
            if estilo_e in estilos_exigidos:
                estilo_count[estilo_e] -= 1
                # Se não há mais deste estilo, decrementar contador
                if estilo_count[estilo_e] == 0:
                    estilos_presentes -= 1
            
            esquerda += 1
    
    # Imprimir resultado
    print(f"Menor trecho tem {melhor_tamanho} shows:")
    for i in range(melhor_inicio, melhor_fim):
        nome, estilo = shows[i]
        print(f"- {nome} ({estilo})")

main()