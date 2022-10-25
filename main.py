# external libraries
from dotenv import load_dotenv
# internal libraries
from super_hero_api import get_random_heros
from heros import TeamBuilder
from simulation import Simulation
from mailer import send_results

if __name__ == "__main__":
    load_dotenv('.env') 
    print("--Welcome to KuTo fighting simulator--")
    print("Loding the heroes...")
    total_heroes = get_random_heros(amount_of_heros=6)
    builder = TeamBuilder()
    half_heroes = len(total_heroes) // 2
    
    team_A = builder.create_team(id="A", heroes=total_heroes[:half_heroes])
    team_B = builder.create_team(id="B", heroes=total_heroes[half_heroes:])
    print("Teams created!")
    print("Starting the simulation...")
    simulation = Simulation()
    simulation.run_simulation(team_A, team_B)
    print(f"The winner team is: {simulation.winner}")
    body = simulation.logs
    if send_results(body=body):
        print("Results sent!")
    



