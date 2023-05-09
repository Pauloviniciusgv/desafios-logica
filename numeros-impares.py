import random

#       Teste de lógica de programação - Estruturas de dados (nível intermediário)
#       Escreva uma função que receba uma lista de números e retorne uma nova lista contendo apenas
#os números ímpares da lista original.

def gera_lista():
    numeros_aleatorios = []
    for i in range(1, 11):
        num = random.randint(1,100)
        numeros_aleatorios.append(num)
    print(numeros_aleatorios)
    return numeros_aleatorios

def filtra_impares(numeros):
    numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))
    print(numeros_impares)

filtra_impares(gera_lista())