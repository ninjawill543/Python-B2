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
    
mot = "Coucou !"
    
for car in mot:
    print(car)
    
if ("Lisa" in eleves):
    print("Alex est présent")
    
print("o" in "Python")
print("Thomas" in eleves)
print("Lise" in eleves)

# range()

# nb_list = [0, 1, 2, 3, 4, 5, 5]


for i in range(100, -1, -2):
    print(f"Mouton n° {i}")
    
eleves = ["Thomas", "Lisa", "Helene", "Patrick", "Paul"]
i = 1
for eleve in eleves:
    eleves[i - 1] = f"Eleve n°{i}: {eleve}"
    i += 1
    
print(eleves)

eleves = ["Thomas", "Lisa", "Helene", "Patrick", "Paul"]

for (i, prenom) in enumerate(eleves):
    eleves[i] = f"Eleve n°{i + 1}: {prenom}"
    # print(i)
    # print(prenom)
    
# print(eleves)