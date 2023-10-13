eleves = ["chump", "oi", "jedfujwedw", "juan", "ojui"]

print (eleves)

notes = [1.5, 77, 20, 6.5, 9]
print(notes)

dates = []


print(len(notes))


print(notes[0])
print(notes[-3])


print (eleves)
print(notes)

eleves.append("juan")
notes.append(20)
print (eleves)
print(notes)

eleves.remove("juan")
eleves.pop(3)

#slicing

jours =[1, 2, 3, 4, 5, 6, 7]
oui = jours[0:5]
print (oui)

weekend = jours[5:]
print(weekend)

#tableaux n-dimension

jours_fr_en = [["lun", "mar", "mer", "jeud", "ven", "sam", "dim"],["mon", "tue", "wed", "thu", "fri", "sat", "sun"]]

print(jours_fr_en)

image = [
    [[16,125,255], ".", ".", ".",".", ".", ".", ".",".", "."],
    [".", ".", ".", ".",".", ".", ".", ".",".", "."],
    [".", ".", ".", ".",".", ".", ".", ".",".", "."],
    [".", ".", ".", ".",".", ".", ".", ".",".", "."],
    [".", ".", ".", ".",".", ".", ".", ".",".", "."],
    [".", ".", ".", ".",".", ".", ".", ".",".", "."],
    [".", ".", ".", ".",".", ".", ".", ".",".", "."],
    [".", ".", ".", ".",".", ".", ".", ".",".", "."],
    [".", ".", ".", ".",".", ".", ".", ".",".", "."],
    [".", ".", ".", ".",".", ".", ".", ".",".", "."],
]

# les chaines de caractere sont des tableaux

chaine = "oui oui baguette"
print (chaine[-1])