# super_hero_api.py

"""This manage the api requests."""
# external libraries
import requests
# external libraries
from numpy import random as np_rand
import os
# internal libraries
from .constants import TOTAL_HEROES


def get_random_heros(amount_of_heros: int = 10) -> list:
    """Recives the amount of unique heroes to be returned and returns a list of them."""
    hero_list = []
    HERO_API_KEY = os.getenv('HERO_API_KEY')

    if not HERO_API_KEY:
        raise ValueError('HERO_API_KEY not found in .env file')

    for id in np_rand.permutation(TOTAL_HEROES)[:amount_of_heros]:
        try:
            response = requests.get(
                f"https://superheroapi.com/api/{HERO_API_KEY}/{id}")
            hero_list.append(response.json())
        except:
            # we stop the loop because this should be a error of the api
            raise Exception(f"Error: Could not get hero of id: {id}.")
            
    return hero_list
