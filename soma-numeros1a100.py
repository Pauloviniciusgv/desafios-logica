#          Teste de lógica de programação - Algoritmos (nível básico)
#          Escreva um programa que calcule a soma dos números de 1 a 100.

numeros = []

for i in range(1,101):
    numeros.append(i)

soma = sum(numeros)
print(numeros)
print("A soma dos numeros de 1 a 100 é =",soma)