# Criação da classe dog que dará origem a varios 'dogs (cachorros)
class Dog:
    # Criação da função __init__ que é respontavel por inicializar o objeto que será criado, esta sendo pedindo o nome e a idade do Dog no momento em que ele é criado 
    # Usamos o termo self para fazer uma refencia a propria classe, portanto quando criar o DOG e passar o nome e a idade, elas pertenceram a classe 'dog
    def __init__(self, name , age):
        self.name = name
        self.age = age
    
    def data_dog(self):
        print(self.name)
        print(self.age)

    def sit(self):
        print("Sentou")

    def roll_over(self):
        print("Rolou")            


'''Convenções:
    - Nome de classe SEMPRE terá a primeira letra Maiuscula
    - Nome de variavel e metodo (função): SEMPRE começa com letras maiusculas
    - Contantes sempre teram suas letras maiusculas'''