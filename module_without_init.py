variavel = 'variável do módulo'


class ClasseSemInit:
    variavel = 'variável da classe'

    def muda_valor(self):
        self.variavel = 'variável inicializada'
        return self.variavel

    @staticmethod
    def printa_variavel():
        variavel = 'variável do método'
        return variavel
