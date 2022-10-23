# external libraries
from typing import List, Optional
from pydantic import BaseModel
# internal libraries
from ..hero import Hero
from .team import  Team

class TeamBuilder(BaseModel):
    heroes: Optional[List[Hero]] = []
    alignment: Optional[str] = None

    def create_team(self, heroes: List[Hero]) -> Team:
        self.reset()
        # Creating the team
        self.alignment = self._set_alignment(heroes)
        self.heroes = self._create_heros(heroes)
        self._set_filiation_coeficient()
        self._update_stats()
        self._set_hp()
        return Team(heroes=self.heroes, alignment=self.alignment)

    def reset(self):
        self.heroes = []
        self.alignment = None

    def _create_heros(self, heroes: List[Hero]):
        """ Create the heros object with the initial values """
        created_heros = []
        for hero in heroes:
            args = {
                'id': hero['id'],
                'name': hero['name'],
                'alignment': hero['biography']['alignment'],
                'intelligence': hero['powerstats']['intelligence'],
                'strength': hero['powerstats']['strength'],
                'speed': hero['powerstats']['speed'],
                'durability': hero['powerstats']['durability'],
                'power': hero['powerstats']['power'],
                'combat': hero['powerstats']['combat'],
            }
            for stat in ["intelligence", "strength", "speed", "durability", "power", "combat"]:
                if args[stat] == 'null':
                    args[stat] = 0
                else:
                    args[stat] = int(args[stat])

            created_heros.append(Hero(**args))
        return created_heros

    def _set_alignment(self, heroes: List[Hero]):
        alignments = [hero['biography']['alignment'] for hero in heroes]
        if alignments.count('good') > alignments.count('bad'):
            self.alignment = 'good'
            return 'good'
        elif alignments.count('good') < alignments.count('bad'):
            self.alignment = 'bad'
            return 'bad'
        else:
            raise ValueError("Cant´t create a team with equal number of good and bad heros")

    def _set_filiation_coeficient(self):
        """Set the filiation coeficient of the heros acording to its team alignment"""
        for hero in self.heroes:
            hero.set_filiation_coeficient(self.alignment)

    def _update_stats(self):
        """Update de stats of the heros acording to its filiation coeficient and actual stamina"""
        for hero in self.heroes:
            for stat in ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']:
                intial_value = getattr(hero, stat)
                setattr(
                    hero,
                    stat,
                    self._stat_modifier(intial_value, hero))

    def _stat_modifier(self, initial_value, hero):
        """Modify the specific stat of the heros acording to the base formula"""
        new_base_value = (initial_value * 2 + hero.actual_stamina)/1.1
        return hero.filiation_coeficient * new_base_value

    def _set_hp(self):
        """ Calculates the initial hp of the hero"""
        for hero in self.heroes:
            hp = (
                hero.strength*0.8 +
                hero.durability*0.7 +
                hero.power) / 2
            hp = hp * (1 + hero.actual_stamina/10) + 100
            hero.initialize_hp(hp)


