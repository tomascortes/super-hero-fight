# Hero Fight simulator
Simulator of a hero fight based on its stats
# Installation

You need to crate a ```.env``` file and add the variable 

``` API_KEY = "your_api_key" ```

install the requierments from the ```requirments.txt``` file.

# Assumntions

Given the description of the tasks. I assumed that the fights where 1 vs 1. For the simplicity of the problem, they will fight in turns. Starting the hero with grater speed. In case both have the same speed, its randomly selected.

- When the fight ends, the winner recovers its health and its able to fight again.

- When some stat was null, it is equivalent to 0.

- the recalculation of stats it is done before the calculation of HP


# TODO
función suelo en formulas hp y stats
privatizar stats, y FB

