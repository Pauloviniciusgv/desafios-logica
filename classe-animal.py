"""Teste de lógica de programação - Programação Orientada a Objetos (nível avançado)
1. Crie uma classe chamada "Animal" com atributos de nome e idade e métodos de comer e dormir.
2. Crie uma classe chamada "Cachorro" que herda da classe "Animal" e adiciona um método de latir.
3. Crie uma classe chamada "Gato" que herda da classe "Animal" e adiciona um método de miar.

4. Crie uma classe chamada "Pessoa" com atributos de nome e idade e um método de falar.
5. Crie uma classe chamada "DonoDeAnimais" que herda da classe "Pessoa" e adiciona um atributo de
animais (uma lista de objetos da classe "Animal") e métodos para adicionar e remover animais da lista."""


class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome} Idade: {self.idade}"

    def comer(self):
        print("Comendo!!")

    def dormir(self):
        print("Dormindo!!")

class Cachorro(Animal):
    def latir(self):
        print("Latindo!!")

class Gato(Animal):
    def miar(self):
        print("Miando!!")

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome} Idade: {self.idade}"

    def falar(self):
        print("Falando !!")

class DonoDeAnimais(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.animais = []

    def adciona_animal(self, animal):
        self.animais.append(animal)

    def remove_animal(self, animal):
        self.animais.remove(animal)

