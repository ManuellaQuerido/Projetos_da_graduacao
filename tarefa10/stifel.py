def stifel(n, k, memo=None):

    if memo is None:
        memo = {}
    
    if (n, k) in memo:
        return memo[(n, k)]
    
    if k == 0 or k == n:        # Caso base
        return 1

    resp1 = stifel(n - 1, k - 1, memo)
    resp2 = stifel(n - 1, k, memo)
    
    resultado = resp1 + resp2
    memo[(n, k)] = resultado
    return resultado

def main():
    n, k = map(int, input().split())
    resultado = stifel(n, k)
    print(resultado)

main()