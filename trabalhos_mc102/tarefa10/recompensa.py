def recompensa(n, x, jogadas_rest=None, memo=None):
    if memo is None:
        memo = {}

    if jogadas_rest is None:
        jogadas_rest = n

    if (x, jogadas_rest) in memo:
        return memo[(x, jogadas_rest)]

    if x == 0:      # Caso base -> Maria chegou!
        return 1.0
    elif jogadas_rest == 0:    # Caso base -> sem jogadas restantes
        return 0.0

    probabilidade_total = 0.0
    for lado in range(1, 7):
        if x - lado > 0:
            probabilidade_total += (1/6) * recompensa(n, x - lado, jogadas_rest - 1, memo)
        elif x - lado == 0:
            probabilidade_total += (1/6)

    memo[(x, jogadas_rest)] = probabilidade_total
    return probabilidade_total

def main():

    n, x = map(int, input().split())

    resultado = recompensa(n, x)
    print(f"{resultado:.3f}")

main()