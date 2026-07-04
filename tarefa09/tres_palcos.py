def main():
    n = int(input())
    shows = []
    duracao = []

    for _ in range(n):
        linha = input().split()
        nome = linha[0]
        duracao_show = int(linha[1])
        shows.append(nome)
        duracao.append(duracao_show)

    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + duracao[i]
    
    melhor_score = (float('inf'), 0, 0)
    melhor_config = None

    for i in range(1, n - 1):
        for j in range(i + 1, n):
            palco1_duracao = prefix_sum[i]
            palco2_duracao = prefix_sum[j] - prefix_sum[i]
            palco3_duracao = prefix_sum[n] - prefix_sum[j]

            max_duracao = max(palco1_duracao, palco2_duracao, palco3_duracao)
            score = (max_duracao, -i, -(j - i))

            if score < melhor_score:
                melhor_score = score
                melhor_config = (i, j)

    i, j = melhor_config

    palco1_shows = shows[:i]
    palco2_shows = shows[i:j]
    palco3_shows = shows[j:]

    palco1_duracao = prefix_sum[i]
    palco2_duracao = prefix_sum[j] - prefix_sum[i]
    palco3_duracao = prefix_sum[n] - prefix_sum[j]

    max_duracao = melhor_score[0]

    print(f"Palco 1: {', '.join(palco1_shows)} ({palco1_duracao} minutos)")
    print(f"Palco 2: {', '.join(palco2_shows)} ({palco2_duracao} minutos)")
    print(f"Palco 3: {', '.join(palco3_shows)} ({palco3_duracao} minutos)")
    print(f"Duração do festival: {max_duracao} minutos")

main()