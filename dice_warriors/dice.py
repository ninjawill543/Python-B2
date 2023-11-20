import random

class Dice:
    def __init__(self, faces=6):
        self._faces = faces

    def __str__(self):
        return f"Bruh this many faces: {self._faces}"

    def roll(self):
        return random.randint(1, self._faces)
 

class RiggedDice(Dice):
    def roll(self, oui = False):
        if (oui == True):
            return 3
        else:
            return super().roll()

if __name__ == "__main__":
    a_dice = RiggedDice()
    print(a_dice.roll())
        
