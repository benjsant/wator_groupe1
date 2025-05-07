import random
from entity.fish import Fish
from entity.clown_fish import ClownFish
from utils.config import *

class Shark(Fish):
    """
    Classe représentant les requins

        - SHARK_REPRODUCTION_TIME : temps de reproduction par défaut des requins
        - chronon_shark : représente le temps qui s'écoule pour le requin (un chronon = une action)
        - shark_energy : energie des requins -> à 0 il meurt
        - alive : booléen indiquant si le requin est vivant ou non
        - img : représentation graphique du requin

    """    

    SHARK_REPRODUCTION_TIME: int = shark_reproduction_time # Modifiable dans utils/config.py 
    img: str = "🦈"
    
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.chronon_shark: int = 0
        self.shark_energy: int = shark_starting_energy # Modifiable dans utils/config.py
        self.alive: bool = True
        

    def move(self, grid) -> None:
        '''
            On commence par incrémenter leurs chronons.
            On définit les 4 directions, et on les rend aléatoires.
            On parcourt une fois les directions dans une boucle pour vérifier si il y a un poisson 
            a proximité pour le faire passer en priorité et le manger.
            Si il n'y a pas de poisson, on refait une boucle pour choisir une case aléatoire parmis les cases vides.
            On termine ces boucles en vérifiant si ils sont encore en vie après leur action.
        
        '''
        self.chronon_shark_one_turn()

        # on définit les 4 directions, puis on les rend aléatoires
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x = (self.x + dx) % len(grid[0]) # on définit x et y pour la nouvelle position, avec effet de tore
            new_y = (self.y + dy) % len(grid)
            neighbor = grid[new_y][new_x] # on définit la cellule voisine avec ces x et y

            # On vérifie d'abord si un poisson est voisin pour le faire passer en priorité
            if isinstance(neighbor, ClownFish):
                neighbor.alive = False  # on indique que le poisson n'est plus en vie
                grid[new_y][new_x] = " " # pour supprimer le poisson
                self.eat()  # le requin se nourrit
                grid[self.y][self.x] = " "  # on supprime le requin de son emplacement
                self.x = new_x  # x et y prennent leur nouvelle valeur
                self.y = new_y
                grid[new_y][new_x] = self   # le requin est positionné sur son nouvel emplacement
                self.is_alive(grid=grid)    # on vérifie son énergie et si il est toujours en vie
                return
        
        # si pas de poisson voisin, déplacement aléatoire
        for dx, dy in directions:
            new_x = (self.x + dx) % len(grid[0])
            new_y = (self.y + dy) % len(grid)

            if grid[new_y][new_x] == " ": # On vérifie si l'emplacement est libre
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
       self.shark_energy += energy_by_eating # modifiable dans utils/config.py


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
            
