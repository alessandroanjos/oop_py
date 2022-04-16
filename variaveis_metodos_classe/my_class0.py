class MinhaClasse:

    estatico = 'Papel' # Variavel de classe

    def __init__(self, estado) -> None:
        self.estado = estado
    
    def print_estatico(self):
        print(self.estatico)

    def mudar_estatico(self):
        self.estatico = 'Pedreiro'


obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

obj1.estado = 'Pedra'
obj2.estado = 'Pedra 2'
print(obj1.estado)
print(obj2.estado)

MinhaClasse.estatico = 'Tesoura'

print(obj1.estatico)
print(obj2.estatico)