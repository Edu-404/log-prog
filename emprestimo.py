renda_mensal = float(input("Digite sua renda mensal: "))
score = int(input("Digite o seu score: "))
possui_restricao = False
possui_restricao = input("Possui restrição, sim ou não? ")

if possui_restricao == 'sim':
    possui_restricao = True
else:
    possui_restricao = False

if score >= 700 and renda_mensal >= 4000.00 and not possui_restricao:
    print("Aprovado!")
elif (renda_mensal >= 2500.00 and possui_restricao) or (score >= 500 and renda_mensal > 6000.00):
    print('Sendo averiguado possível aprovação... ')
else:
    print("Recusado!")