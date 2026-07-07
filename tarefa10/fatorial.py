def fatorial_base(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_base(n - 1)
    
def main():
    n = int(input())
    resultado = fatorial_base(n)
    print(resultado)

main()