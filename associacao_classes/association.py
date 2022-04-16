''''Relacionamento de Associacao'''

from typing import Type


class Interruptor:

    def __init__(self, comodo: str) -> None:
        self.__comodo = comodo
        self.__acesso = False

    
    def acender(self):
        self.__acesso = True
        print('Acendendo o comodo: {}'.format(self.__comodo))


    def apagar(self):
        self.__acesso = False
        print('Apagando o comodo: {}'.format(self.__comodo))

    def get_acesso(self):
        return self.__acesso

    def get_comodo(self):
        return self.__comodo


class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()
    

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    
    def dormir(self, interruptor: Type[Interruptor]):
        if interruptor.get_acesso() == True:
            print('O interruptor "{}" está ligado. Desligue antes de dormir!'.format(interruptor.get_comodo()))
        else:
            print('Fui dormir')
        

interruptor_sala = Interruptor('Sala')
interruptor_quarto = Interruptor('Quarto')

interruptor_quarto.acender()

andressa = Pessoa()

andressa.acender_luz(interruptor_quarto)
andressa.apagar_luz(interruptor_quarto)
andressa.dormir(interruptor_quarto)

