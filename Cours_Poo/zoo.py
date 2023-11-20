class Animal:
    def __init__(self, nom):
        self.nom=nom
        print(f"Création d'un animal nommé {self.nom}")

    def nourrir(self):
        print("Vérifier que l'animal est vivant")
        print("Calul du stock")
        print("Début de l'alimentation de l'animal")


class Chat(Animal):
    def nourrir(self):
        super().nourrir()
        print("Petit calin")

class Requin(Animal):
    def nourrir(self):
        super().nourrir()
        print("On reste a distance")

class Licorne(Animal):
    pass

minou=Chat("meow")
croc = Requin("croc")
hhhh = Licorne("horn")

animaux= [minou, croc, hhhh]

animal: Animal
for animal in animaux:
    animal.nourrir()