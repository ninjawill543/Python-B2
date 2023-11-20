from character import Character
from dice import Dice


if __name__ == "__main__":
    char1 = Character("Tom", 20, 8, 3, Dice())
    char2 = Character("Laetitia", 20, 8, 3, Dice())
    
    while (char1.is_alive() and char2.is_alive()):
        damages = char1.attack()
        char2.defense(damages)
        
        damages = char2.attack()
        char1.defense(damages)