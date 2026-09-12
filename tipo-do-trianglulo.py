ladoA = float(input("Digite o lado A do triângulo: "))
ladoB = float(input("Digite o lado B do triângulo: "))
ladoC = float(input("Digite o lado C do triângulo: "))

# Feito pelo professor
# variavel condicao retorna um valor booleano
condicao = (
    (ladoA + ladoB > ladoC) and
    (ladoA + ladoC > ladoB) and
    (ladoB + ladoC > ladoA)
)

if condicao:
    if ladoA == ladoB == ladoC:
        print("Equilatero")
    elif ladoA != ladoB != ladoC:
        print("Escaleno")
    # elif (ladoA == ladoB or
    #       ladoA == ladoC or ladoB == ladoC):
    #     print("Isosceles")
    else:
        print("Isosceles")
else:
    print('Não é um triangulo')


# Feito por mim
# if a + b > c and a + c > b and b + c > a:
#     print('É um triangulo válido')
#     if a == b and b == c:
#         print("Seu triângulo é Equilátero")
#     elif a == b or a == c or b == c:
#         print("Seu triângulo é Isósceles")
#     elif a != b and b != c:
#         print("Seu triângulo é Escaleno")
# else:
#     print('Valores inválidos')
