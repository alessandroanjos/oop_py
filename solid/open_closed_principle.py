
''' Meyer`s Open-Closed principle
Sejam fáceis de mudar, devem ser projetados para permitir o comportamento desses sistemas 
s serem alterados pela adição de novo código, em vez de alterar os existentes no código '''

'''
Módulo é um elemento coeso que possui uma certa funcionalidade.

- Um módulo será considerado fechado se estiver disponível para uso por outros módulos
- Um módulo será considerado aberto se ainda estiver disponível para extensão. 
'''

# Motivacao: Entradas diferentes, geram acoes diferentes


class Circo1:
    ''' Sem o principio de Open-Closed '''
    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaco()

    def apresentar_malabarista(self):
        print('Malabarista se apresentando')

    def apresentar_palhaco(self):
        print('Palhaco se apresentando')



class Circo2:
    ''' Aberta pra extensões, Fechado para modificacoes '''

    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()
        

class Malabarista:

    def apresentar_show(self):
        print('Malabarista se apresentando')


class Palhaco:
    
    def apresentar_show(self):
        print('Palhaco se apresentando')

class Domador:
    
    def apresentar_show(self):
        print('Domador se apresentando')



circo = Circo2()
malabarista = Malabarista()
palhaco = Palhaco()

circo.apresentar(malabarista)
circo.apresentar(palhaco)