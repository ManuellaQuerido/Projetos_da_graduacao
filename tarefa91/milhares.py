def milhar_decrescente():
    m = int(input())

    for numero in range(m):
        numero = int(input())
        mil = numero / 1000
        if mil > 0:
            print(f"{numero} é um milhar-decrescente")
        else:
            print(f"{numero} é um milhar-decrescente")