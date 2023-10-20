choix = "o"
note = 0
moyenne = 0
notes = []
moyenneO = 0
notesO = []

while (choix == "o"):
    note = float(input("Saisissez une note: "))
    moyenne += note
    notes.append(note)

    if (note != 0):
        moyenneO += note
        notesO.append(note)

    

    choix = input("Voulez-vous saisir une nouvelle note? (o/n)")

print(f"Moyenne de la classe: {round(moyenne / len(notes), 2)}")
print(f"Moyenne optimisée de la classe: {round(moyenneO / len(notesO), 2)}")