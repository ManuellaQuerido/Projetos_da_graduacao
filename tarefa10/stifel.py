def stifel(n, k, memo=None):

    if memo is None:
        memo = {}
    
    if (n, k) in memo:
        return memo[(n, k)]
    
    if k == 0 or k == n:        # Caso base
        return 1


def main():
    n, k = map(int, input().split())
    resultado = stifel(n, k)
    print(resultado)

main()