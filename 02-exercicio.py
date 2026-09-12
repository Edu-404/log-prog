num1 = int(input('Digite um número: '))
num2 = int(input('Digite um outro número: '))
num3 = int(input('Digite mais um outro número: '))

if num1 > num2 and num1 > num3:
    print("O primeiro número é o maior")
elif num2 > num3:
    print("O segundo número é o maior")
else:
    print("O terceiro número é o maior")