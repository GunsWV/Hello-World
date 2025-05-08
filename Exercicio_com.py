nota1 =int(input('insira primeira nota:'))

nota2 =float(input('insira segunda nota:'))

nota3 =int(input('insira terceira nota:'))

nota4 =float(input('insira quarta nota:'))

#calculo de media
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 5:
    print("Aprovado")
else:
    print("Reprovado")
    