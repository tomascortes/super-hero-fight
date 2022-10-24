# external libraries
from typing import List, Optional
from pydantic import BaseModel
from random import shuffle
# internal libraries
from ..hero import Hero

class Team(BaseModel):
    id: str
    heroes: List[Hero]
    alignment: str

    def is_alive(self) -> bool:
        for hero in self.heroes:
            if hero.is_alive():
                return True
        return False

    def get_fighter(self) -> Hero:
        shuffle(self.heroes)
        for hero in self.heroes:
            if hero.is_alive():
                return hero

    def __str__(self):
        output = f"Team alignment: {self.alignment}\n"
        for hero in self.heroes:
            output += "----------\n"
            output += "Name: " + hero.name + "\n"
            output += "HP: " + str(hero.hp) + "\n"
            output += "FB: " + str(hero.alignment) + "\n"
            output += "Strength: " + str(hero.strength) + "\n"
        return output

