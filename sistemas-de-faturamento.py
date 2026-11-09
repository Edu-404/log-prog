class Produto():
    def __init__(self, nome, preco, quantidade=0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    @property
    def preco(self):
        return self._preco

    @property
    def quantidade(self):
        return self._quantidade

    @property
    def valor_total_estoque(self):
        return self._preco * self._quantidade

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self._preco = novo_preco
        else:
            print('Erro. O valor não pode ser igual ou menor do que 0.')

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:
            self._quantidade = nova_quantidade
        else:
            print('Erro. O valor não pode ser menor do que 0.')

    def adicionar_estoque(self, qtd):
        self.quantidade += qtd
        print('Quantidade adicionada')

    def remover_estoque(self, qtd):
        resultado = self.quantidade - qtd
        if resultado > 0:
            self.quantidade -= qtd
            print('Quantidade removida')
        else:
            print('Não há saldo suficiente para ser removido')

p1 = Produto('Celular', 1850.95, 5)

print(p1.nome)
print(p1.preco)
print(p1.quantidade)
print(p1.valor_total_estoque)
p1.preco = 1570.50
p1.quantidade = 8
print(p1.preco)
print(p1.quantidade)
print(p1.valor_total_estoque)
p1.adicionar_estoque(3)
print(p1.quantidade)
p1.remover_estoque(5)
print(p1.quantidade)
