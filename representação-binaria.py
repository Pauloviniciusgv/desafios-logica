#            Teste de lógica de programação - Algoritmos (nível básico)
#            Escreva um programa que leia um número inteiro e imprima sua representação binária.

numero = int(input("Digite um numero inteiro :"))
representacao_binaria = bin(numero)
numero_binario = representacao_binaria[2:]
print(numero_binario)
