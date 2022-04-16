class Pessoa:

    def __init__(self, nome) -> None:
        self.__local = None
        self.__nome = nome
    
    def entrar_no_local(self):
        self.__local.acender_luzes()

    
    def apresentar_local(self):
        endereco = self.__local.get_endereco()
        print(endereco)
    
    def se_apresentar(self):
        print('Olá, eu sou o {}'.format(self.__nome))


    def set_local(self, local: any):
        self.__local = local


    def get_local(self):
        return self.__local
