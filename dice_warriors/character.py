from __future__ import annotations
from dice import Dice

print("\n")


class Character:
    
    def __init__(self, name: str, max_health: int, attack: int, defense: int, dice) -> None:
        self._name = name
        self._max_health = max_health
        self._current_health = max_health
        self._attack_value = attack
        self._defense_value = defense
        self._dice = dice
        
    def __str__(self):
        return f"I'm {self._name} the Character with attack: {self._attack_value} and defense: {self._defense_value}"
    
    def is_alive(self):
        # return bool(self._current_health)
        return self._current_health > 0
        
    def decrease_health(self, amount):
        self._current_health -= amount
        self.show_healthbar()
        
    def show_healthbar(self):
        missing_hp = self._max_health - self._current_health
        healthbar = f"[{"🥰" * self._current_health}{"🖤" * missing_hp}] {self._current_health}/{self._max_health}hp"
        print(healthbar)

    def attack(self, target: Character):
        damages = self._attack_value + self._dice.roll()
        print(f"{self._name} attack with {damages} damages in your face ! (attack: {self._attack_value} + roll: {damages - self._attack_value})")
        target.defense(damages)
    
    def defense(self, damages):
        roll = self._dice.roll()
        wounds = damages - self._defense_value - roll
        print(f"{self._name} take {wounds} wounds in his face ! (damages: {damages} - defense: {self._defense_value} - roll: {roll})")
        self.decrease_health(wounds)


if __name__ == "__main__":
    a_dice = Dice(6)

    character1 = Character("Gerard", 20, 8, 3, Dice(6))
    character2 = Character("Lisa", 20, 8, 3, Dice(6))
    print(character1)
    print(character2)
    
    while(character1.is_alive() and character2.is_alive()):
        character1.attack(character2)
        character2.attack(character1)
