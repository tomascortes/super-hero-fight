# external libraries
from dotenv import load_dotenv
import os
# internal libraries
from super_hero_api import get_random_heros
 

if __name__ == "__main__":
    # Use load_env to trace the path of .env:
    load_dotenv('.env') 
    print(get_random_heros())