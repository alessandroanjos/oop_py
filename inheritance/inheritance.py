
class Mae:

    def __init__(self, endereco: str) -> None:
        self.endereco = endereco
        self.sobrenome = 'da Silva'

    def comer(self) -> None:
        print('Estou comendo')

    def estudar(self) -> None:
        print('Estou estudando')


class Filha(Mae):

    def __init__(self) -> None:
        super().__init__('Rua das Goaiabeiras')

    def brincar(self, brinquedo: str):
        print('Estou brincando com o/a {}'.format(brinquedo))


class Neta(Filha):

    def __init__(self, endereco) -> None:
        super().__init__(endereco)


ana = Mae('Rua da praia')
print(ana.endereco)

clarissa = Filha()
clarissa.brincar('Barbie')
print(clarissa.endereco)


