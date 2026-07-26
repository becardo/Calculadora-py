from operacao import Operacao

class Divisao(Operacao):
    def calcular(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        return a / b