print("\n")

eleves = ["Thomas", "Lisa", "Helene", "Patrick", "Paul"]
print(eleves)

notes = [10.5, 12.0, 16.0, 17.5, 4.0]
#          |    |      |    |     |
#          0    1      2    3     4
#                     ...  -2    -1
print(notes)

dates = []

print(len(notes))

print(notes[0])
print(notes[len(notes) - 1])
print(notes[-1])
print(notes[-5])
print(notes[len(notes) * -1])

eleves.append("Lucas")
notes.append(20.0)

print(eleves)
print(notes)

# eleves.remove("Lucas")
# eleves.pop(3)

# Slicing

jours = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]
lun_ven = [jours[0], jours[1], jours[2]]

lun_ven = jours[0:5]
print(lun_ven)

weekend = jours[5:]
print(weekend)

# print(jours[:])

# Tableaux n-dimension

jours_fr_en = [
    ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"],
    ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
]

print(jours_fr_en[1][-2:])

image = [
    [[16, 125, 255], ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
]

# Les chaines de caractère sont des tableaux

chaine = "Coucou j'aime le Python !"
print(chaine)
print(chaine[-1])
print(chaine[-8:])