#!usr/bin/env python3

## Calculadora em python
'''
Como estudo, esse programa consiste na criação de classes que irão compor uma calculadora:
    - soma
    - subtração
    - multiplicação
    - divisão
    - potencia
    - raiz -> A operacao de Raiz tem a sintaxe 'a v b', que significa 'raiz b-ésima de a'. 

Utilização: digitar a expressão no terminal. Exemplo: 5+7, 8*7, 5v3;
            exit encerra a calculadora.
'''

from soma import Soma
from subtracao import Subtracao
from multiplicacao import Multiplicacao
from divisao import Divisao
from potencia import Potencia
from raiz import Raiz

class Calculadora:
    def __init__(self):
        ''' Dicionário de operações. Mais tarde será utilizado para relacionar o operador digitado
        com a classe que deve ser instanciada. '''
        self.operacoes = {
            "+": Soma,
            "-": Subtracao,
            "*": Multiplicacao,
            "/": Divisao,
            "^": Potencia,
            "v": Raiz
        }

    def iniciar(self):
        operadores = ["+", "-", "*", "/", "^", "v"]

        print("Calculadora ligada. Digite Exit a qualquer momento para encerrar a calculadora.")

        while True:
            expressao = input("Digite a expressão: ")

            if expressao.lower() == "exit":
                print("Encerrando a calculadora...")
                break

            for op in operadores:
                if op in expressao:
                    partes = expressao.split(op)
                    break

            classe = self.operacoes[op]
            operacao = classe()

            resultado = operacao.calcular(float(partes[0]), float(partes[1]))
            print("Resultado: ", resultado)

            
calc = Calculadora()
calc.iniciar()
    

