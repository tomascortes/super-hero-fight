# external libraries
from random import randint, choice
from pydantic import BaseModel, PrivateAttr
# internal libraries
from .constants import MAX_AS, MAX_FB_RAND_RANGE

class Hero(BaseModel):
    id: int
    name: str
    alignment: str
    alive: bool = True
    actual_stamina: int = randint(0, MAX_AS)
    filiation_coeficient: float = None
    _hp: int = PrivateAttr()
    _base_hp: int = PrivateAttr()
    # stats
    intelligence: int
    strength: int
    speed: int
    durability: int
    power: int
    combat: int

    def set_filiation_coeficient(self, team_alignment):
        """
        Set the filiation coeficient of the hero acording to its team alignment
        """
        fb = 1 + randint(0, MAX_FB_RAND_RANGE)
        if self.alignment == team_alignment:
            self.filiation_coeficient = fb
        else:
            self.filiation_coeficient = 1/fb
    
    def initialize_hp(self, value):
        self._base_hp = value
        self._hp = value

    @property
    def hp(self):
        return self._hp

    def take_damage(self, damage):
        if damage < 0:
            raise ValueError("Damage cannot be negative")
        self._hp -= damage
        if self._hp < 0:
            self._hp = 0
            self.alive = False

    def regenerate_hp(self):
        self._hp = self._base_hp

    def is_alive(self):
        return self.alive

    def mental_damage(self) -> float:
        damage = (
            self.intelligence*0.7 +
            self.speed*0.2 +
            self.combat*0.1)
        return damage

    def strong_damage(self) -> float:
        damage = (
            self.strength*0.6 +
            self.power*0.2 +
            self.combat*0.2)
        return damage

    def fast_damage(self) -> float:
        damage = (
            self.speed*0.55 +
            self.durability*0.25 +
            self.strength*0.2)
        return damage

    def attack(self) -> float:
        possible_attacks = [
            self.mental_damage,
            self.strong_damage,
            self.fast_damage]
        selected_attack = choice(possible_attacks)
        return selected_attack() * self.filiation_coeficient

    def __str__(self):
        output = f"{self.name} - {self.alignment}\n"
        output += f"HP: {self.hp}\n"
        output += f"Stamina: {self.actual_stamina}\n"
        output += f"FB: {self.filiation_coeficient}\n"
        output += f"Intelligence: {self.intelligence}\n"
        output += f"Strength: {self.strength}\n"
        output += f"Speed: {self.speed}\n"
        output += f"Durability: {self.durability}\n"
        output += f"Power: {self.power}\n"
        output += f"Combat: {self.combat}\n"
        return output

        
