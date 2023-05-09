#       Teste de lógica de programação - Algoritmos (nível básico)
#       Escreva um programa que calcule a média aritmética de 3 números fornecidos pelo usuário.
print("Preciso que digite 3 numeros!!")
num1 = float(input("Digite o primeiro numero :"))
num2 = float(input("Digite o segundo numero :"))
num3 = float(input("Digite o terceiro numero :"))

numeros = [num1, num2, num3]
soma_dos_numeros = (num1 + num2 + num3)
media = soma_dos_numeros / len(numeros)
print("A média dos três numeros é :", media)