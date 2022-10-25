# external libraries
from pydantic import BaseModel
from typing import Dict, Optional
# internal libraries
from heros import Team


class Simulation(BaseModel):
    teams: Optional[Dict[str,Team]] = {}
    
    winner: Optional[str] = None
    logs: Optional[str] = ""

    def run_simulation(self, team_a: Team, team_b: Team):
        self.reset()
        # teams simulation
        self.teams[team_a.id] = team_a
        self.teams[team_b.id] = team_b
        figth_counter = 1
        while team_a.is_alive() and team_b.is_alive():
            fighters = [team_a.get_fighter(), team_b.get_fighter()]
            fighters.sort(key=lambda x: x.speed, reverse=True)
            self.prestentation_fight(figth_counter, fighters)

            turn = 0
            while fighters[0].is_alive() and fighters[1].is_alive():
                # Attacker
                damage = fighters[turn].attack()
                fighters[not turn].take_damage(damage)
                self.print_turn(fighters, turn, damage)
                turn = not turn


            if fighters[0].is_alive():
                fighters[0].regenerate_hp()
                self.save_print(f"{fighters[0].name} won the fight")
            else:
                fighters[1].regenerate_hp()
                self.save_print(f"{fighters[1].name} won the fight")
            
            figth_counter += 1

        if team_a.is_alive():
            self.winner = team_a.id
        else:
            self.winner = team_b.id
        self.store_winners()

    def reset(self):
        self.teams = {}

    def print_teams(self):
        for team in self.teams.values():
            print(team)
    
    def prestentation_fight(self, figth_counter, fighters):
        self.save_print(f"\nFight number {figth_counter}")
        self.save_print(f"Fighters: {fighters[0].name}[HP {round(fighters[0].hp, 3)}] vs {fighters[1].name}[HP {round(fighters[1].hp, 3)}]")

    def print_turn(self, fighters, turn, damage):
        print(f"turn {turn}: {fighters[turn].name} attacks with: {round(damage, 3)}")
        print(f"turn {turn}: {fighters[not turn].name} HP: {round(fighters[not turn].hp, 3)}")
    
    def save_print(self, text):
        self.logs += text + "\n"
        print(text)

    def store_winners(self):
        self.logs += "<strong>"
        self.logs += "\nWINNER TEAM\n"
        for hero in self.teams[self.winner].heroes:
            self.logs += f"{hero.name}:"
            if hero.is_alive():
                self.logs += " O\n"
            else:
                self.logs += " X\n"
        self.logs += "</strong>"

                
                

