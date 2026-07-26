from operacao import Operacao

class Raiz(Operacao):
    def calcular(self, a, b):
        return a ** (1/b)