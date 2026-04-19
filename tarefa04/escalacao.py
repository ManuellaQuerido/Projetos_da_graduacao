n = int(input())

jogadores = []
total_gols = []
jogos = []

datas = []
gols_por_datas = []

i = -1

for j in range(n):
    linha = input().split()

    nome = linha[0]
    data = linha[1]
    gols = int(linha[2])

#Datas
    for a in range(len(datas)):
        if datas[a] == data:
            i = a
            break
    if i != -1:
        gols_por_datas[i] += gols
    else:
        datas.append(data)
        gols_por_datas.append(gols)

#Jogadores
    for a in range(len(jogadores)):
        if jogadores[a] == nome:
            i = a
            break
    if i != -1:
        total_gols[i] += gols
        jogos[i] += 1
    else:
        jogadores.append(nome)
        total_gols.append(gols)
        jogos.append(1)

#Calcular o maximo de gols
if len(gols_por_datas) > 0:
    melhor = gols_por_datas[0]
    for valor in gols_por_datas:
        if valor > melhor:
            melhor = valor
else:
    melhor = 0
    
#Escalação
escalados = input().split()
gols_esperados = 0

for nome in escalados:
    for a in range(len(jogadores)):
        if jogadores[a] == nome:
            i = a
            break
    if i != -1:
        media = total_gols[i] / jogos[i]
        gols_esperados += media

print (f"Melhor placar recente: {melhor}")
print(f"Número de gols esperados: {gols_esperados:.1}")