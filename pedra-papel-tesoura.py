import random

hand = ["pedra", "papel", "tesoura"]
myHand = input('Escolha a sua mão: ')
myHand = myHand.lower()
machineHand = random.choice(hand)
# machineHand = hand[random.randint(0, len(hand) - 1)]

# print(f'\nSua mão é {myHand}, a mão da máquina é {machineHand}\n')

if myHand not in hand:
    print('Inválido')
elif myHand == 'pedra' and machineHand == 'papel':
    print('Papel cobre pedra. A máquina ganhou!')
elif myHand == 'pedra' and machineHand == 'tesoura':
    print('Pedra quebra tesoura. Você ganhou!')
elif myHand == 'papel' and machineHand == 'tesoura':
    print('Tesoura corta papel. A máquina ganhou!')
elif myHand == 'papel' and machineHand == 'pedra':
    print('Papel cobre pedra. Você ganhou!')
elif myHand == 'tesoura' and machineHand == 'pedra':
    print('Pedra quebra tesoura. A máquina ganhou')
elif myHand == 'tesoura' and machineHand == 'papel':
    print('Tesoura corta papel. Você ganhou!')
else:
    print('Empate')