# Hero Fight simulator 🦇 
Simulator of an epic battle between tho teams made of heroes 🦸‍♀️ and villains 🦹

# Installation
You need to create a ```.env``` file and add the variable 
``` 
HERO_API_KEY="hero_api_key" 
MAIL_GUN_API_KEY="mailgun_api_key
```

Install the requirements from the ```requirments.txt``` file.
``` 
pip install -r requirments
``` 

# Execution
To run the code, you need to execute:
``` 
python main.py
``` 

# Assumptions
Given the description of the tasks. I assumed that the fights were 1 vs 1. For the simplicity of the problem, they will fight in turns. Starting the hero with grater speed. In case both have the same speed, it's randomly selected.

- When the fight ends, the winner recovers its health and It's able to fight again.

- When some stat was null, it is equivalent to 0.

- the recalculation of stats it is done before the calculation of HP

- In case of neutral heroes, causing a tie at the moment of defining the alignment of the team, i say that the good heroes will convince the neutral to be a good team.
