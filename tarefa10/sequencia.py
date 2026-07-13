def sequencia(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        Pn = sequencia(n - 1) + 2 * sequencia(n - 2) + 3 * sequencia(n - 3)
        return Pn
        
def main():
    n = int(input())

    resultado = sequencia(n)
    print(resultado)

main()