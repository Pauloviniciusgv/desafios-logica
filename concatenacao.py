#       Teste de lógica de programação - Estruturas de dados (nível intermediário)
#       Escreva uma função que receba uma lista de strings e retorne uma única string que seja a
#concatenação de todas as strings da lista.

lista_strings = ["banana", "maracujá", "uva", "limão", "abacaxi"]
def concatena(lista_strings):
    lista_concatenada = " ".join(lista_strings)
    lista_concatenada = lista_concatenada.title()
    print(lista_concatenada)

concatena(lista_strings)