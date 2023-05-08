variavel = 'variável do módulo'


class ClasseComInit:
    variavel = 'variável da classe'

    def __init__(self):
        self.variavel = 'variável não inicializada'

    def muda_valor(self):
        self.variavel = 'variável inicializada'
        return self.variavel
