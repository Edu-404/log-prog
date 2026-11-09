class Aluno():
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    @property
    def nota(self):
        return self._nota

    def aprovado(self):
        if self.nota >= 6.0:
            return True
        else:
            return False

    @nota.setter
    def nota(self, nova_nota):
        if 0.0 <= nova_nota <= 10.0:
            self._nota = nova_nota
        else:
            print('Erro. Alteração rejetada.')

a1 = Aluno('Gil', 8)

print(f'Nome do aluno: {a1.nome}')
print(f'Nota do aluno: {a1.nota}')
print(f'Aprovado? {a1.aprovado()}')
a1.nota = 5
print(f'Nota do aluno: {a1.nota}')
print(f'Aprovado? {a1.aprovado()}')





        