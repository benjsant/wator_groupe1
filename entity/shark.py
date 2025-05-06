import random
from entity.fish import Fish
from entity.clown_fish import ClownFish
from utils.config import *


class Shark(Fish):
    """
    Classe représentant les requins
    Valeurs fixes et communes à toutes les instances de Shark 
    (Utilisation d'attributs de classe et non d'instance car mieux pour l'optimisation de la mémoire)

        - MAX_SHARK_REPRODUCTION_TIME : temps de reproduction par défaut des requins
        - shark_reproduction_time : timer de reproduction des requins (à 0 -> nouveau requin)
        - shark_energy : energie des requins -> à 0 il meurt
        - alive : booléen indiquant si le requin est vivant ou non
        - img : représentation graphique du requin

    """    

    SHARK_REPRODUCTION_TIME: int = shark_reproduction_time #Temps de reproduction des requins. Modification dans utils/config.py 
    img: str = "🦈"
    
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.chronon_shark: int = 0
        self.shark_energy: int = 8
        self.alive: bool = True
        

    def move(self, grid) -> None:
        '''
            On définit les 4 directions, et on les rend aléatoires.
            On parcourt une fois les directions dans une boucle pour vérifier si il y a un poisson 
            a proximité pour le faire passer en priorité et le manger.
            Si il n'y a pas de poisson, on refait une boucle pour choisir une case aléatoire parmis les cases vides.
        
        '''
        self.chronon_shark_one_turn()

        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x = (self.x + dx) % len(grid[0])
            new_y = (self.y + dy) % len(grid)
            neighbor = grid[new_y][new_x]

            if isinstance(neighbor, ClownFish):
                neighbor.alive = False
                grid[new_y][new_x] = " " # pour supprimer le poisson
                self.eat()
                grid[self.y][self.x] = " "
                self.x = new_x
                self.y = new_y
                grid[new_y][new_x] = self
                self.is_alive(grid=grid)
                return
        
        for dx, dy in directions:
            new_x = (self.x + dx) % len(grid[0])
            new_y = (self.y + dy) % len(grid)

            if grid[new_y][new_x] == " ":
                grid[self.y][self.x] = " "
                self.x = new_x
                self.y = new_y
                grid[new_y][new_x] = self
                self.is_alive(grid=grid)
                return

        
        
        

    def eat(self) -> None:
       '''
            Lorsque le requin mange, on augmente son énergie
       '''
       self.shark_energy += 3


    def reproduce(self, x, y) -> object|None:  
        """
            Fonction gérant la reproduction des requins
            Lorsque les chronons du requins atteignent son âge de reproduction,
            on crée un nouveau requin, et les chronons sont réinitialisés

        """        

        if self.chronon_shark >= self.SHARK_REPRODUCTION_TIME:
            self.chronon_shark = 0
            return Shark(x = x, y = y)
        return None
        

    def chronon_shark_one_turn(self):
        """ 
            Fonction incrémentant les chronons du requin
        """
        self.chronon_shark += 1
    

    def is_alive(self, grid):
        """Fonction vérifiant si le requin est toujours en vie
        Si la variable shark_energy tombe à 0, le requin disparaît

        Args:
            grid (list):  Grid (list of list), environnement dans lequel évolue le requin
        """
        self.shark_energy -= 1
        if self.shark_energy <= 0:
            grid[self.y][self.x] = " "
            self.alive= False
            
