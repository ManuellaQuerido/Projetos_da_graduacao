def fatorial(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        fat = n * fatorial(n - 1)
        return fat
    
def main():
    n = int(input())
    resultado = fatorial(n)

    print(resultado)

main()