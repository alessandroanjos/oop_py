class Pessoa:

    def __init__(self, comportamento) -> None:
        self.comportamento = comportamento
    
    def realizar_acao(self):
        self.comportamento.acao()