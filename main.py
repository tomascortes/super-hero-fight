# external libraries
from dotenv import load_dotenv
import os
# internal libraries
from super_hero_api import get_random_heros
from heros import TeamBuilder
 

if __name__ == "__main__":
    load_dotenv('.env') 
    total_heroes = get_random_heros(amount_of_heros=6)
    builder = TeamBuilder()
    team_A = builder.create_team(total_heroes[:3])
    # team_B = builder.create_team(total_heroes[3:])
    print(team_A)
    # print(team_B)

