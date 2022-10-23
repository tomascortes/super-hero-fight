# external libraries
from typing import List, Optional
from pydantic import BaseModel
# internal libraries
from ..hero import Hero

class Team(BaseModel):
    heroes: List[Hero]
    alignment: str

    def __str__(self):
        output = f"Team alignment: {self.alignment}\n"
        for hero in self.heroes:
            output += "----------\n"
            output += "Name: " + hero.name + "\n"
            output += "HP: " + str(hero.hp) + "\n"
            output += "FB: " + str(hero.alignment) + "\n"
            output += "Strength: " + str(hero.strength) + "\n"
        return output

