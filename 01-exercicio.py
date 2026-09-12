firstNote = float(input('Digite a primeira nota: '))
secondNote = float(input('Digite a segunda nota: '))
media = (firstNote + secondNote) / 2

if media < 6:
    print("Aluno Reprovado")
else:
    print("Aluno Aprovado")