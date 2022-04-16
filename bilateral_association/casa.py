class Casa:

    def __init__(self) -> None:
        self.__endereco = 'Rua da Aurora'
        self.__proprietario = None

    
    def acender_luz(self):
        print('Estou acendendo as luzes')

    def get_endereco(self):
        return self.__endereco

    def set_proprietario(self, proprietario: any):
        self.__proprietario = proprietario
    
    def get_proprietario(self):
        return self.__proprietario