from acoes.correr import FazerCorrida
from acoes.falar import IniciarFala
from pessoa_comportamento import Pessoa


# Injecao da dependencia aqui / Incluindo o pattern Factory
julia = Pessoa(IniciarFala())
julia.realizar_acao()


joaquim = Pessoa(FazerCorrida())
joaquim.realizar_acao()
