def mdc(a, b):

    if b == 0:
        return a

    else:
        resto = a % b
        return mdc(b, resto)

def main():
    a, b = map(int, input().split())

    resultado = mdc(a, b)
    print(resultado)

main()