jogador1 = print("Pedra, Papel ou Tesoura: ")
jogador2 = print("Pedra, Papel ou Tesoura: ")

if jogador1 == jogador2:
    print("Empate")
elif ( (jogador1 == 'Papel' and jogador2 == 'Pedra')
    or (jogador1 == 'Pedra' and jogador2 == 'Tesoura')
    or (jogador1 == 'Tesoura' and jogador2 == 'Papel') 
    ):
    print('Jogador ganhou')
