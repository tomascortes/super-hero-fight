from pydantic import BaseModel
from typing import List, Optional
from heros import Hero


class Simulation(BaseModel):
    team_a: Optional[List[Hero]] = []
    team_b: Optional[List[Hero]] = []
    winner: Optional[str] = None

    def run_simulation(self, team_a: List[Hero], team_b: List[Hero]) -> None:
        self.reset()
        # teams simulation
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
                print(f"{fighters[0].name} won the fight")
            else:
                fighters[1].regenerate_hp()
                print(f"{fighters[1].name} won the fight")
            
            figth_counter += 1

        if team_a.is_alive():
            self.winner = "Team A"
        else:
            self.winner = "Team B"

    def reset(self):
        self.team_a = []
        self.team_b = []

    def print_teams(self):
        print("Team A")
        print(self.team_a)
        print("Team B")
        print(self.team_b)
    
    def prestentation_fight(self, figth_counter, fighters):
        print(f"\nFight number {figth_counter}")
        print(f"Fighters: {fighters[0].name}[HP {round(fighters[0].hp, 3)}] vs {fighters[1].name}[HP {round(fighters[1].hp, 3)}]")

    def print_turn(self, fighters, turn, damage):
        print(f"turn {turn}: {fighters[turn].name} attacks with: {round(damage, 3)}")
        print(f"turn {turn}: {fighters[not turn].name} HP: {round(fighters[not turn].hp, 3)}")

