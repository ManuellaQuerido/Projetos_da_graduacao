def milhar_decrescente():
    n_atual = n % 1000
    n //= 1000

    while n > 0:
        n_proximo = n % 1000

        if n_proximo >= n_atual:
            return False
        
        n_proximo == n_atual:
            n //= 1000
    return True

def main():
    m = int(input())

    for i in range(m):
        numero = int(input())

        if milhar_decrescente(numero):
            print(f"{numero} é um milhar-decrescente ")
        else:
            print(f"{numero} não é um milhar-decrescente ")
        
if __name__ == "__main__":
    main()