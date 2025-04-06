from .robo_base import Robo
import random
from random import uniform

class RoboLutador(Robo):
    dano_maximo = 0.12  

    def __init__(self, nome: str):
        super().__init__(nome)
        self.poder = round(random.uniform(self.dano_maximo, 1), 2)

    def atacar(self, robo_alvo: 'Robo'):
        if self.vida <= 0:
            print(f"{self.nome} não pode atacar. Está sem vida!")
            return
        
        dano = round(robo_alvo.vida * self.poder, 2)
        robo_alvo.vida = round(max(0, robo_alvo.vida - dano), 2)
        print(f"{self.nome} atacou {robo_alvo.nome} causando {dano:.2f} de dano. Vida do robô {robo_alvo.nome} em {robo_alvo.vida:.2f}")
        
        if isinstance(robo_alvo, RoboLutador) and robo_alvo.vida > 0:
            robo_alvo.atacar(self)
