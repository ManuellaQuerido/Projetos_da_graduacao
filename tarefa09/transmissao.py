def main():
    k = int(input())
    estilos_exigidos = set(input().split())
    
    n = int(input())
    shows = []
    
    for _ in range(n):
        linha = input().split()
        nome = linha[0]
        estilo = linha[1]
        shows.append((nome, estilo))
    
    esquerda = 0
    estilo_count = {}
    estilos_presentes = 0
    
    melhor_inicio = 0
    melhor_fim = n
    melhor_tamanho = n + 1
    
    for direita in range(n):
        nome_d, estilo_d = shows[direita]
        
        if estilo_d in estilos_exigidos:
            if estilo_d not in estilo_count:
                estilo_count[estilo_d] = 0
            
            if estilo_count[estilo_d] == 0:
                estilos_presentes += 1
            
            estilo_count[estilo_d] += 1
        
        # FIX: Adicionar "and esquerda < n" para evitar index out of bounds
        while estilos_presentes == len(estilos_exigidos) and esquerda < n:
            tamanho = direita - esquerda + 1
            
            if tamanho < melhor_tamanho:
                melhor_tamanho = tamanho
                melhor_inicio = esquerda
                melhor_fim = direita + 1
            
            nome_e, estilo_e = shows[esquerda]
            if estilo_e in estilos_exigidos:
                estilo_count[estilo_e] -= 1
                if estilo_count[estilo_e] == 0:
                    estilos_presentes -= 1
            
            esquerda += 1
    
    # Se não encontrou solução válida
    if melhor_tamanho == n + 1:
        print("Nenhum trecho válido encontrado")
        return
    
    palavra_show = "show" if melhor_tamanho == 1 else "shows"
    print(f"Menor trecho tem {melhor_tamanho} {palavra_show}:")
    
    for i in range(melhor_inicio, melhor_fim):
        nome, estilo = shows[i]
        print(f"- {nome} ({estilo})")

main()