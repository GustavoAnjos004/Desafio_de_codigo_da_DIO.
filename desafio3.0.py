name = input("qual o seu nome: ")
age = input("qual sua idade: ")
Type = input("escolha sua clsse (Guerreiro, Mago, Monge ou Ninja): ")

class Hero:
    def __init__(self, name, age, Type):
        self.name = name
        self.age = age
        self.Type = Type

    def atak(self):
        if self.Type == "Mago":
            atak = "magia"
        elif self.Type == "Guerreiro":
            atak = "espada"
        elif self.Type == "Monge":
            atak = "artes marciais"
        elif self.Type == "Ninja":
            atak = "shuriken"
        else:
            atak = "um ataque desconhecido"

        message = f"o {self.Type} {self.name} atacou usando {atak}"
        print(message)


hero1 = Hero(name, age, Type)

hero1.atak()