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