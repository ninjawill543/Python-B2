print("\n")
# f-strings (formatted strings)

date = "26/07/1985"

jour = int(date[:2])
mois = int(date[3:5])
annee = int(date[-4:])

# resultat = jour + "." + mois + "." + annee
# print(resultat)
resultat = f"La date est: {jour}.{mois}.{annee + 100}"
print(resultat)

habitants = 7_753_000_000
superficie = 149_000_000

# round()

print(f"Nb habitant par km²: {round(habitants / superficie, 2)}")