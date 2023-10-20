#class : plan d'immeuble
#objet : immeuble dans la vrai vie
#constructeur : se lance automatiquement quand un objet est crée
#attribut : 

class Voiture:
    # constructeur
    def __init__(self, marque, couleur = "rouge"):
        self.couleur = couleur
        self._vitesse_max = 220
        self.marque = marque
        self.nb_roues = 4
        self.demarree = False
        self._vitesse = 0
        print("\n")
        print("une nouvelle voiture est créée")

    def __str__(self):
        return f"Une {self.marque} {self.couleur} qui roule à une vitesse max de {self._vitesse_max}"

    def demarrer(self):
        if (not self.demarree):
            self.demarree = True
            print("Vroum Vroum lets go\n")

    def avancer(self, vitesse_cible):
        if (self.demarree == True):
            for i in range(vitesse_cible):
                if (self._vitesse + 1 <= self._vitesse_max):
                    self._vitesse += 1
                    print(self._vitesse)
        else:
            print("Il faut démarrer la voiture avant d'avancer")





ma_voiture = Voiture("clio", "bleue")
print(ma_voiture)
ma_voiture.demarrer()
ma_voiture.avancer(200)


ta_voiture = Voiture("dacia")
print(ta_voiture)
ta_voiture.avancer(200)


