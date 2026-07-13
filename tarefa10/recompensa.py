def recompensa(n, x, jogadas_rest=None, memo=None):
    if memo is None:
        memo = {}

    if jogadas_rest in memo:
        jogadas_rest = n  

    if (x, jogadas_rest) in memo:
        return memo[(x, jogadas_rest)]

    if x == 0:
        return 1.0
    elif jogadas_rest == 0:
        return 0.0
    

def main():

    n, x = map(int, input().split())

    resultado = recompensa(n, x)
    print(f"{resultado.:3f}")

main()