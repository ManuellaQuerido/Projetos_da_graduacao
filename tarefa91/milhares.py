def milhar_decrescente():
    m = int(input())

    for numero in range(m):
        numero = int(input())

        if numero > 1000:
            mil = numero / 1000
            if mil > 0:
                centena = numero / 100
                if centena < mil:
                    print(f"{numero} é um milhar-decrescente")
                else:
                    print(f"{numero}não é um milhar-decrescente")
            