import random

class Robo:
    nivel_critico = 0.39

    def __init__(self, nome: str):
        self.nome = nome
        self.__vida = round(random.uniform(0, 1), 2)

    def __repr__(self):
        return f"{self.nome} (Vida: {self.vida:.2f})"

    def __add__(self, outro: 'Robo'):
        pai = self.nome.split('-')[0]
        mae = outro.nome.split('-')[0]
        bebe = f"{pai}-{mae}"
        return type(self)(bebe)

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, valor):
        self.__vida = min(max(valor, 0), 1)

    def precisa_de_medico(self):
        return self.vida < self.nivel_critico
