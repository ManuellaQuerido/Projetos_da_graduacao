jogadores = []
gols = []
assistencias = []

while True:
    try:
        linha = input().split()
        jogadores.append(linha[0])
        gols.append(float(linha[1]))
        assistencias.append(float(linha[2]))
    except:
        break
melhor_valor = -1
melhor_meia = ""
melhor_atacante = ""
melhor_assistencia = -1

n = len(jogadores)
for m in range(n):
    for a in range(n):
        if m != a:
            valor = min(assistencias[m], gols[a])
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_meia = jogadores[m]
                melhor_atacante = jogadores[a]
                melhor_assistencia = assistencias[m]
            elif valor == melhor_valor:
                if assistencias[m] > melhor_assistencia:
                    melhor_meia = jogadores[m]
                    melhor_atacante = jogadores[a]
                    melhor_assistencia = assistencias[m]
print(f"Melhor dupla tem {melhor_meia} e {melhor_atacante} com {melhor_valor:.1f} gols esperados.")