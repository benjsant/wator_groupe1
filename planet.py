from interface.grid_view import GridView
from interface.main_window import MainWindow
from interface.history_window import HistoryWindow
from entity.fish import Fish
from entity.shark import Shark
from entity.clown_fish import ClownFish
import random
from pprint import pprint # pour afficher ligne par ligne dans la console
from PyQt5 import QtCore
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from itertools import zip_longest # pour alterner poissons et requins dans boucle si nombre innégal

class Planet:
    def __init__(self, width:int, height:int):
        """
        class Planet

        Args:
            width (int): _description_ la largeur de la liste
            height (int): _description_ la hauteur de la liste
        """
        self.width=width
        self.height=height
        self.grid=self.init_grid()
        self.chronon=0
        self.sharks = []
        self.fishes = []
        
    def init_grid(self)->list:
        """_summary_
        fonction qui initialize le monde 2 dimension

        Returns:
            list: retourne une variable a 2 dimension pour acceder grid[x][y]
        """
        """"""
        return [[" " for col in range(self.height)]for row in range(self.width)]  
        
                
    def display_planet(self) -> list:
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

        display = self.init_grid()
        for x in range(len(self.grid)): # pour chaque colonne
            for y in range(len(self.grid[0])): # pour chaque ligne
                cell = self.grid[x][y]
                if isinstance(cell, Shark):
                    display[x][y] = cell.img
                elif isinstance(cell, ClownFish):
                    display[x][y] = cell.emoji_fish
                else:
                    display[x][y] = " "
        return display
    


    def random_init_pos(self, nb_shark: int, nb_fishes: int):
        # On y ajoute les requins de façon aléatoire (par objet), en vérifiant si la position est valide
        for _ in range(nb_shark):
            while True:
                x = random.randrange(self.width)
                y = random.randrange(self.height)
                if self.is_valid_position(x=x, y=y):
                    shark = Shark(x=x, y=y)
                    self.new_shark(shark)
                    break

        # Même chose avec les poissons
        for _ in range(nb_fishes):
            while True:
                x = random.randrange(self.width)
                y = random.randrange(self.height)
                if self.is_valid_position(x=x, y=y):
                    fish = ClownFish(x=x, y=y)
                    self.new_fish(fish)
                    break
        


    def update(self)->None:
        self.chronon += 1


    def new_fish(self, fish):
        """Fonction permettant l'instanciation d'un nouveau poisson.
        Appelle la fonction is_valid_position pour vérifier si la position est valide ou non,
        puis vérifie par sécurité si le nombre de poissons ne dépasse pas le nombre de case
        de la grille.

        Args:
            fish (ClownFish): l'objet ClownFish que l'on veut créer avec ses coordonnées

        Returns:
            _type_: None si position invalide ou poissons trop nombreux, sinon ClownFish
        """

        if not self.is_valid_position(x=fish.x, y=fish.y):
            return None
        if len(self.fishes) >= (self.width * self.height):
            return None
        self.fishes.append(fish)
        self.grid[fish.x][fish.y] = fish


    def new_shark(self, shark):
        """Fonction permettant l'instanciation d'un nouveau requin.
        Appelle la fonction is_valid_position pour vérifier si la position est valide ou non,
        puis vérifie par sécurité si le nombre de requins ne dépasse pas le nombre de case
        de la grille.

        Args:
            shark (Shark): l'objet Shark que l'on veut créer avec ses coordonnées

        Returns:
            _type_: None si position invalide ou requins trop nombreux, sinon Shark
        """

        if not self.is_valid_position(x=shark.x, y=shark.y):
            return None
        if len(self.sharks) >= (self.width * self.height):
            return None
        self.sharks.append(shark)
        self.grid[shark.x][shark.y] = shark



    def is_valid_position(self, x, y) -> bool:
        """Fonction indiquant si la position indiquée est valide ou non

        Args:
            x (int): largeur de la grille
            y (int): hauteur de la grille

        Returns:
            bool: True si position valide et libre, sinon False
        """
        if x >= self.width or y >= self.height:
            return False
        else:
            if self.grid[x][y] == " ":
                return True
            else:
                return False
            


    """ BOUCLE PRINCIPALE """
    def run_simulation(self):

        pprint(self.display_planet())

        while True:

            # Liste prête à accueillir les bébés requins ou poissons
            new_sharks = []
            new_fishes = []

            # Boucle alternant entre requins et poissons
            # On les fait se déplacer, puis on gère leur reproduction
            entities = list(zip_longest(self.sharks, self.fishes))
            for shark, fish in entities:
                if shark:
                    shark_x = shark.x
                    shark_y = shark.y
                    shark.move(self.grid)
                    # Gestion de la reproduction
                    baby_shark = shark.reproduce(x=shark_x, y=shark_y)
                    if baby_shark and self.is_valid_position(baby_shark.x, baby_shark.y):
                        self.grid[baby_shark.x][baby_shark.y] = baby_shark
                        new_sharks.append(baby_shark)

                if fish:
                    fish_x = fish.x
                    fish_y = fish.y
                    fish.move(self.grid)
                    baby_fish = fish.reproduce(x = fish_x, y = fish_y)
                    if baby_fish and self.is_valid_position(baby_fish.x, baby_fish.y):
                        self.grid[baby_fish.x][baby_fish.y] = baby_fish
                        new_fishes.append(baby_fish)

            # Ajout des nouveaux poissons / requins
            self.sharks.extend(new_sharks)
            self.fishes.extend(new_fishes)

            # On update pour ne garder que les entités vivantes
            self.sharks = [shark for shark in self.sharks if shark.alive]
            self.fishes = [fish for fish in self.fishes if fish.alive]

            self.update() # incrémentation des chronons
            print(f"Tour n°{self.chronon}")
            pprint(self.display_planet())


            # VERIFICATIONS NBRE REQUINS / POISSONS
            print(f"Fishes : {len(self.fishes)}")
            print(f"Sharks : {len(self.sharks)}")

            num_clownfish = 0
            num_shark = 0
            for row in range(len(self.grid)):
                for col in range(len(self.grid[row])):
                    cell=self.grid[row][col]
                    if(isinstance(cell,ClownFish)):
                        num_clownfish += 1
                    if(isinstance(cell,Shark)):
                        num_shark += 1

            print("Poissons dans la grille : ", num_clownfish)
            print("Requins dans la grille : ", num_shark)


            for x in range(self.width):
                for y in range(self.height):
                    entity = self.grid[x][y]
                    if isinstance(entity, ClownFish) and entity not in self.fishes:
                        print(f"🐠 Problème détecté à la position ({x},{y}) : poisson non listé.")


            # FIN BOUCLE
            print("")
            print("")

            if len(self.sharks) == 0 or self.chronon >= 30:
                break
