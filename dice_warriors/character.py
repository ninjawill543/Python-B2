from dice import Dice


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
        healthbar = f"[{'●' * self._current_health}{'○' * missing_hp}] {self._current_health}/{self._max_health}hp"
        print(healthbar)

    def attack(self):
        damages = self._attack_value + self._dice.roll()
        print(damages)

if __name__ == "__main__":
    a_dice = Dice(6)
    print(a_dice)

    character1 = Character("Gerard", 20, 8, 3, Dice(6))
    print(character1)
    
    character1.decrease_health(3)
    character1.attack()