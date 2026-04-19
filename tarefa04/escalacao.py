n = int(input())

jogadores = []
total_gols = []
jogos = []

datas = []
gols_por_datas = []

for j in range(n):
    linha = input().split()

    nome = linha[0]
    data = linha[1]
    gols = int(linha[2])
    
    i_data = -1
    for i in range(len(datas)):
        if datas[i] == data:
            i_data = i
        gols_por_datas[i_data] += gols
    else:
        datas.append(data)
        gols_por_datas.append(gols)
    
    if nome in jogadores:
        i_jogador = jogadores.index(nome)
        total_gols[i_jogador] += gols
        jogos[i_jogador] += 1
    else:
        jogadores.append(nome)
        total_gols.append(gols)
        jogos.append(1)

if gols_por_datas:
    melhor = max(gols_por_datas)
else:
    melhor = 0
    
escalados = input().split()
gols_esperados = 0

for nome in escalados:
    if nome in jogadores:
        i = jogadores.index(nome)
        media = total_gols[i] / jogos[i]
        gols_esperados += media

print (f"Melhor placar recente: {melhor}")
print(f"Número de gols esperados: {gols_esperados}")