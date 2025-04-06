from .robo_base import Robo
import random

class RoboMedico(Robo):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.poder_de_cura = round(random.uniform(0, 1), 2)

    def curar(self, outro_Robo: 'Robo'):
        if self.vida < outro_Robo.vida:
            print(f"{self.nome} não pode curar {outro_Robo.nome}, pois tem menos vida.")
            return
        
        if not outro_Robo.precisa_de_medico():
            print(f"{outro_Robo.nome} não precisa de cura.")
            return
        
        cura = min(self.poder_de_cura, 1 - outro_Robo.vida)
        outro_Robo.vida = round(outro_Robo.vida + cura, 2)
        print(f"{self.nome} curou {outro_Robo.nome} em {cura:.2f}. Vida atual: {outro_Robo.vida:.2f}")
