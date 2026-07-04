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
                estilo_count[estilo_d]

            if estilo_count[estilo_d] == 0:
                estilos_presentes += 1
                
            estilo_count[estilo_d] += 1