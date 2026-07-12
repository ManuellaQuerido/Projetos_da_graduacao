'''
Problema: Mostrar se o aluno foi aprovado, reprovado ou se está de recuperação

algoritmo:
    leia nota1
    leia nota2

    calcular a média das notas

    Se a média for maior ou igual a 5.0:
        Se a média for maior que 7.0:
            imprima "Aprovado"
        Senão:
            imprima "Recuperação"
    Senão:
        imprima "Reprovado"

'''

n1 = float(input())
n2 = float(input())

média = (n1 + n2)/2

if média >= 5.0:
    if média >= 7.0:
        print("Aprovado")
    else:
        print("Recuperação")
else:
    print("Reprovado")