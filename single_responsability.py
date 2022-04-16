
class SistemaCadastral:
    '''Exemplo sem o uso do Single Responsibility Principle'''
    def cadastrar(self, nome: str, idade: int):
        if isinstance(nome, str) and isinstance(idade, int):
            print('acessando o banco de dados')
            print('Cadastrar o usuário: {}, idade {} '.format(nome, idade) )
        else:
            print('dados inválidos')



class SistemaCadastralSRP:
    '''Exemplo com o uso do Single Responsibility Principle'''
    def cadastrar(self, nome: str, idade: int):
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_erro()


    def __verificar_dados(self, nome, idade):
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False

    
    def __armazenar_usuario(self, nome:str, idade:int):
        print('acessando o banco de dados...')
        print('Cadastrar o usuário: {}, idade {} '.format(nome, idade) )

    
    def __indicar_erro(self):
        print('dados inválidos')