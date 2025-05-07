from entity.fish import Fish
from utils.config import *
import random


class ClownFish(Fish):
    """
    Classe représentant les poissons-clown

        - REPRODUCTION_TIME : temps de reproduction par défaut des poissons-clowns
        - chronon_fish : représente le temps qui s'écoule pour le poisson (un chronon = une action)
        - alive : booléen indiquant si le poisson est vivant ou non
        - emoji_fish : représentation graphique du poisson-clown

    """    
    
    REPRODUCTION_TIME: int = fish_reproduction_time #Temps de reproduction des poissons. Modification dans utils/config.py 
    emoji_fish: str = "🐠"

    def __init__(self,x :int, y :int):
        super().__init__(x, y)
        self.chronon_fish: int = 0
        self.alive: bool = True

    def move(self, grid)->None: 
        """
            Déplace l'entité vers une case voisine vide dans la grille. 
            Le mouvement est aléatoire parmi les directions possibles (haut, bas, gauche, droite) 
            et utilise un système de coordonnées toroidal pour gérer les bords de la grille.

            Args:
                grid (list of list): La grille de simulation, où chaque case peut contenir 
                                    une entité ou être vide (None).

            Returns:
                None: La méthode modifie directement la position de l'entité dans la grille.
        """
        
        self.chronon_fish_one_turn()

        # on définit les 4 directions, puis on les rend aléatoires
        directions=[(0,1), (1,0), (0,-1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x = (self.x + dx) % len(grid[0]) # on définit x et y pour la nouvelle position, avec effet de tore
            new_y = (self.y + dy) % len(grid)

            if grid[new_y][new_x] == " ":  # On vérifie si l'emplacement est libre
                grid[self.y][self.x] = " " # on supprime le poisson de son emplacement
                self.x = new_x  # x et y prennent leur nouvelle valeur
                self.y = new_y
                grid[new_y][new_x] = self   # le poisson est positionné sur son nouvel emplacement
                return
    

    def reproduce(self, x, y) -> object|None:
        """
                Vérifie si le poisson peut se reproduire en fonction de son temps de reproduction. 
                Si le poisson a atteint son temps de reproduction, un nouvel objet ClownFish est créé 
                à la même position. Sinon, la méthode retourne None.

                Returns:
                    Fish or None: Un nouvel objet ClownFish si le poisson peut se reproduire, 
                                sinon None.
        """
        if self.chronon_fish >= self.REPRODUCTION_TIME:
            self.chronon_fish = 0
            return ClownFish(x = x, y = y)
        return None
        
    def chronon_fish_one_turn(self): 
        """_summary_
            Le poisson gagne un chronom 
        """
        self.chronon_fish += 1