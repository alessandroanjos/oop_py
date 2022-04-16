from pessoa import Pessoa
from casa import Casa

casa_de_rosa = Casa()
ana = Pessoa('Ana')

ana.set_local(casa_de_rosa)
casa_de_rosa.set_proprietario(ana)


proprietario = casa_de_rosa.get_proprietario()
proprietario.se_apresentar()

ana.apresentar_local()