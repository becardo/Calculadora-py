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

        print("=====================================================================================")
        print("Calculadora ligada. Digite Exit a qualquer momento para encerrar a calculadora.")
        print("\n\nOperações possíveis: " \
        "\n + -- Soma " \
        "\n - -- Subtração " \
        "\n * -- Multiplicação " \
        "\n / -- Divisão " \
        "\n ^ -- Potência" \
        "\n v -- Raiz" \
        "\n\n OBS: A operacao de Raiz tem a sintaxe 'a v b', que significa 'raiz b-ésima de a'. ")
        print("=====================================================================================")

        while True:
            print("\n~~~~~~~~~~~~~~~~~~~~")
            expressao = input("Digite a expressão: ")

            if expressao.lower() == "exit":
                print("--> Encerrando a calculadora...")
                break

            find_op = False
            erro = False
            
            for op in operadores:
                if op in expressao:
                    find_op = True
                    partes = expressao.split(op)

                    if len(partes) != 2 or partes[0] == "" or partes[1] == "":
                        print("--> Expressão inválida! Por favor, digite a expresão no formato ' a op b'.")
                        erro = True
                        break

                    try:
                        a = float(partes[0])
                        b = float(partes[1])
                    except ValueError:
                        print("--> Erro! Os valores devem ser números.")
                        erro = True
                        break

                    break

            if erro:
                continue

            if not find_op:
                print("--> Operação inválida! Escolha uma operação dentro do escopo.")
                continue

            classe = self.operacoes[op]
            operacao = classe()

            try:
                resultado = operacao.calcular(a, b)
                print("Resultado: ", resultado)
                print("~~~~~~~~~~~~~~~~~~~~")
            except ZeroDivisionError as e:
                print(e)

            
calc = Calculadora()
calc.iniciar()
    

