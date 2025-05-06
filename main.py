from interface.grid_view import GridView
from interface.main_window import MainWindow
from interface.history_window import HistoryWindow
from entity.fish import Fish
from entity.shark import Shark
from entity.clown_fish import ClownFish
from planet import Planet
import random
from pprint import pprint # pour afficher ligne par ligne dans la console
from PyQt5 import QtCore
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from itertools import zip_longest # pour alterner poissons et requins dans boucle si nombre innégal



""" SETTINGS """

number_of_fishes = 12
number_of_sharks = 20

rows = 15
columns = 15


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
        
# test de Mainwindows
app = QApplication(sys.argv)
main = MainWindow(test_world,GridView,ClownFish,Shark,HistoryWindow)
main.show()
sys.exit(app.exec())
main.update()

""" DISPLAY TERMINAL """

def display_planet(grid: list) -> list:
    """ Fonction permettant l'affichage de la grille 2D et ses éléments
        On parcourt toute la grille :
        - rencontre objet Shark -> affichage emoji requin
        - rencontre objet ClownFish -> affichage emoji poisson
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

    # Liste prête à accueillir les bébés requins ou poissons
    new_sharks = []
    new_fishes = []

    # Boucle alternant entre requins et poissons
    # On les fait se déplacer, puis on gère leur reproduction
    entities = list(zip_longest(test_world.sharks, test_world.fishes))
    for shark, fish in entities:
        if shark:
            shark_x = shark.x
            shark_y = shark.y
            shark.move(test_world.grid)
            # Gestion de la reproduction
            baby_shark = shark.reproduce(x=shark_x, y=shark_y)
            if baby_shark and test_world.is_valid_position(baby_shark.x, baby_shark.y):
                test_world.grid[baby_shark.x][baby_shark.y] = baby_shark
                new_sharks.append(baby_shark)

        if fish:
            fish_x = fish.x
            fish_y = fish.y
            fish.move(test_world.grid)
            baby_fish = fish.reproduce(x = fish_x, y = fish_y)
            if baby_fish and test_world.is_valid_position(baby_fish.x, baby_fish.y):
                test_world.grid[baby_fish.x][baby_fish.y] = baby_fish
                new_fishes.append(baby_fish)

    # Ajout des nouveaux poissons / requins
    test_world.sharks.extend(new_sharks)
    test_world.fishes.extend(new_fishes)

    # On update pour ne garder que les entités vivantes
    test_world.sharks = [shark for shark in test_world.sharks if shark.alive]
    test_world.fishes = [fish for fish in test_world.fishes if fish.alive]

    test_world.update() # incrémentation des chronons
    print(f"Tour n°{test_world.chronon}")
    pprint(display_planet(test_world.grid))


    # VERIFICATIONS NBRE REQUINS / POISSONS
    print(f"Fishes : {len(test_world.fishes)}")
    print(f"Sharks : {len(test_world.sharks)}")

    num_clownfish = 0
    num_shark = 0
    for row in range(len(test_world.grid)):
        for col in range(len(test_world.grid[row])):
            cell=test_world.grid[row][col]
            if(isinstance(cell,ClownFish)):
                num_clownfish += 1
            if(isinstance(cell,Shark)):
                num_shark += 1

    print("Poissons dans la grille : ", num_clownfish)
    print("Requins dans la grille : ", num_shark)



    # FIN BOUCLE
    print("")
    print("")

    if len(test_world.sharks) == 0 or test_world.chronon >= 30:
        break