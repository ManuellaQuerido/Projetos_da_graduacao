def recompensa(n, x):


def main():

    n, x = map(int, input().split())

    resultado = recompensa(n, x)
    print(f"{resultado.:3f}")

main()