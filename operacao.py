from abc import ABC, abstractmethod

class Operacao(ABC):
    '''Uma classe abstrata diz: qualque classe que herda de mim é 
    obrigada a implementar o método 'calcular' '''

    @abstractmethod
    def calcular(self, a, b):
        pass