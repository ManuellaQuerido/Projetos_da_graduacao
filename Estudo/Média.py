notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

media = (notaA + notaB) / 2

if media >= 7.0:
    print("média: %.1f - Aprovado"% media)
else:
    print("Media: %.1f - Reprovado "% media)