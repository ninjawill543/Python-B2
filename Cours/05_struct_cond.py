print("\n")
# if (condition):
    # instruction (dans le cas où condition est vrai)
    
age = int(input("Quel est votre âge ?"))

# ==
# !=
# >
# >=
# <
# <=

if (age < 18):
    print("Statut mineur : Remise de 15%")
elif (age >= 18) and (age < 70):
    print("Statut voyageur : Tu payes")
elif (age >= 70):
    print("Statut sénior : Remise de 10%")
    
bool
True
False

mineur = True
if (age > 18):
    mineur = False
    
mineur = age > 18