import random
#   Teste de lógica de programação - Estruturas de dados (nível intermediário)
#   Escreva uma função que receba uma lista de números e retorne a soma de todos os elementos da lista.

def gera_lista():
    numeros_aleatorios = []
    for i in range(1, 6):
        num = random.randint(1,100)
        numeros_aleatorios.append(num)
    print(numeros_aleatorios)
    return numeros_aleatorios

def soma_lista(numeros_aleatorios):
    soma = sum(numeros_aleatorios)
    print(soma)

soma_lista(gera_lista())