import random
#           Teste de lógica de programação - Estruturas de dados (nível intermediário)
#           Escreva uma função que receba uma lista de números e retorne o maior número da lista.

def gera_lista():
    numeros_aleatorios = []
    for i in range(1, 6):
        num = random.randint(50,100)
        numeros_aleatorios.append(num)
    print(numeros_aleatorios)
    return numeros_aleatorios

def maior_numero(numeros_aleatorios):
    maior = max(numeros_aleatorios)
    print("O maior número é :", maior)


maior_numero(gera_lista())