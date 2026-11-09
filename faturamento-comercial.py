class Produto():
    def __init__(self, nome, preco, quantidade=0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco <= 0:
            False
        else:
            self._preco = novo_preco