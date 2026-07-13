def mdc(a, b):
    
    if b == 0:
        return a

    else:
        quociente = a % b
        return mdc(b, quociente)

def main():
    a = map(int, input().split())
    b = map(int, input().split())

    resultado = mdc(a, b)
    print(resultado)

main()