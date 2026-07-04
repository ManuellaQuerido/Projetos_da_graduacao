def main():
    n = int(input())
    shows = []
    duracao = []

    for i in range(n):
        linha = input().split()
        nome = linha[0]
        duracao_show = int(linha[1])
        shows.append(nome)
        duracao.append(duracao_show)

    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + duracao[i]
    
    melhor_max = float('inf')
    melhor_config = None

    for i in range(1, n - 1):
        for j in range(i + 1, n):
            palco1_duracao = prefix_sum[i]
            palco2_duracao = prefix_sum[j] - prefix_sum[i]
            palco3_duracao = prefix_sum[n] - prefix_sum[j]

            max_duracao = max(palco1_duracao, palco2_duracao, palco3_duracao)

            if (max_duracao < melhor_max or (max_duracao == melhor_max and i > melhor_config[0]) or (max_duracao == max_duracao and i == melhor_config[0] and (j - i) > (melhor_config[1] - melhor_config[0]))):
                melhor_max = max_duracao
                melhor_config = (i, j)