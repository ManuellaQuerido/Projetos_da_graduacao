def milhar_decrescente():
    n_atual = n % 1000
    n //= 100

    while n > 0
    for numero in range(m):
        numero = int(input())

        if numero > 0:
            dezena = numero / 10
            centena = numero / 100
            mil = numero / 1000

            if mil > centena and mil > dezena:
                print(f"{numero} é um milhar-decrescente")
            elif mil > centena and mil < dezena:
                print(f"{numero}não é um milhar-decrescente")
            