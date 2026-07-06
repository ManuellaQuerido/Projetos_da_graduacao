lista_nomes = []
nome = input()
while nome != "-":
    lista_nomes.append(nome)
    nome = input()

# guardar as iniciais
lista_iniciais = []
for nome in lista_nomes:
    inicial = nome[0]
    if inicial not in lista_iniciais:
        lista_iniciais.append(inicial)

print(" ".join(lista_iniciais))
#print(sum([1,2,3], 52))

#lista_compras = []
#valor = float(input())
#while valor >= 0:
#    lista_compras.append(valor)
#    valor = float(input())

#soma = 0.0
#for valor in lista_compras:
#    soma += valor
#print(soma)

#n = int(input())
#for i in range(n):
 #   print(i)
  #  i += 1

#n = int(input("Digite quantos amigos você tem? "))
#amigos = []
#i = 0
#for i in range(n):
#    nome = input(f"Digite o nome do amigo número {i}: ")
#    amigos.append(nome)
#    i += 1

#j = int(input("Digite um número: "))
#print(f"Seu amigo número {j} chama-se {amigos[j]}")

for i in range(1, 11):
    for j in range(10 - i):
        print(" ", end="")
    for j in range(2 * i):
        print("*", end="")
    for j in range(10 - i):
        print(" ", end="")
    print()