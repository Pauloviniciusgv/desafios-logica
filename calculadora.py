print("***** CALCULADORA SIMPLES!! *****")
num1 = float(input("Digite o primeiro número:"))
operacao = input("[-]Subtração [+]Adição [*]Multiplicação [/]Divisão | "
                 "Qual operação deseja fazer ? ")
num2 = float(input("Digite o segundo número:"))

def adicao(x,y):
    return x+y

def subtracao(x,y):
    return  x-y

def divisao(x,y):
    return x/y

def multiplicacao(x,y):
    return x*y

operacoes = {
    "+": adicao,
    "-": subtracao,
    "/": divisao,
    "*": multiplicacao
}

resultado = operacoes[operacao](num1,num2)

if operacao in operacoes:
    print(f'O resultado da operação é = {resultado}')
else:
    print("Operação inválida!!")