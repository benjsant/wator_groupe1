from entity.fish import Fish
from entity.shark import Shark
from entity.clown_fish import ClownFish
from planet import Planet
import random
from pprint import pprint # pour afficher ligne par ligne dans la console



""" SETTINGS """

number_of_fishes = 8
number_of_sharks = 5

rows = 8
columns = 8


""" GENERATE """
# On crée le milieu de la simulation
test_world = Planet(width=columns, height=rows)

# On y ajoute les requins de façon aléatoire (par objet), en vérifiant si la position est valide
for _ in range(number_of_sharks):
    while True:
        x = random.randrange(columns)
        y = random.randrange(rows)
        if test_world.is_valid_position(x=x, y=y):
            shark = Shark(x=x, y=y)
            test_world.new_shark(shark)
            break

# Même chose avec les poissons
for _ in range(number_of_fishes):
    while True:
        x = random.randrange(columns)
        y = random.randrange(rows)
        if test_world.is_valid_position(x=x, y=y):
            fish = ClownFish(x=x, y=y)
            test_world.new_fish(fish)
            break
        


""" DISPLAY TERMINAL """

def display_planet(grid: list) -> list:
    """ Fonction permettant l'affichage de la grille 2D et ses éléments
        On parcourt toute la grille :
        - rencontre objet Shark -> affichage emoji requin
        - rencontre objet Clownfish -> affichage emoji poisson
        - sinon rien

    Args:
        grid (list): liste de liste représentant la grille en 2D

    Returns:
        list: liste de liste représentant la grille en 2D
    """

    display = test_world.init_grid()
    for x in range(len(grid)): # pour chaque colonne
        for y in range(len(grid[0])): # pour chaque ligne
            cell = grid[x][y]
            if isinstance(cell, Shark):
                display[x][y] = cell.img
            elif isinstance(cell, ClownFish):
                display[x][y] = cell.emoji_fish
            else:
                display[x][y] = " "
    return display


""" BOUCLE PRINCIPALE """

pprint(display_planet(test_world.grid))
while True:
    for fish in test_world.fishes:
        fish.move(test_world.grid)

    for shark in test_world.sharks:
        shark.move(test_world.grid)

    test_world.chronon += 1
    print(f"Tour n°{test_world.chronon}")
    pprint(display_planet(test_world.grid))
    print("")
    print("")

    if len(test_world.sharks) == 0 or test_world.chronon >= 20:
        break
    
