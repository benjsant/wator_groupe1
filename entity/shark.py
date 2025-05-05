import random
from entity.fish import Fish
from entity.clown_fish import ClownFish
from planet import Planet

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

    SHARK_REPRODUCTION_TIME: int = 12
    chronon_shark: int = 0
    shark_energy: int = 8
    alive: bool = True
    img: str = "🦈"
    
    
    def __init__(self, x, y):
        super().__init__(x, y)
        

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
            neighbor = grid[new_x][new_y]

            if isinstance(neighbor, ClownFish):
                grid[new_x][new_y] = " " # pour supprimer le poisson
                neighbor.alive = False
                self.eat()
                grid[self.x][self.y] = " "
                self.x = new_x
                self.y = new_y
                grid[new_x][new_y] = self
                break
        
        for dx, dy in directions:
            new_x = (self.x + dx) % len(grid[0])
            new_y = (self.y + dy) % len(grid)

            if grid[new_x][new_y] == " ":
                grid[self.x][self.y] = " "
                self.x = new_x
                self.y = new_y
                grid[new_x][new_y] = self
                break

        self.is_alive(grid=grid)
        
        

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
        else:
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
        if self.shark_energy == 0:
            grid[self.x][self.y] = " "
            self.alive= False
            
