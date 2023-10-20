compteur = 0

while (compteur <= 1000):
    if (compteur % 2 == 0):
        print(compteur)
    compteur = compteur + 1
    
eleves = ["Thomas", "Lisa", "Helene", "Patrick", "Paul"]

i = 0
while (i < len(eleves)):
    print(eleves[i])
    i += 1
    
    
# choix = "o"
# liste_note = []
# moyenne = 0

# while (choix == "o"):
#     note = float(input("Saisissez une nouvelle note : "))
    
#     liste_note.append(note)
#     moyenne = moyenne + note
    
#     choix = input("Voulez-vous saisir une nouvelle note ? (o/n)")
    
# print(f"La moyenne de la classe est {moyenne / len(liste_note)}")

# For

eleves = ["Thomas", "Lisa", "Helene", "Patrick", "Paul"]

for eleve in eleves:
    print(eleve)
    
for car in "Coucou":
    print(car)
    
print("o" in "Python")
print("Thomas" in eleves)
print("Lise" in eleves)

# range()