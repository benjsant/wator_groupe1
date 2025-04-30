import random
from entity.fish import Fish

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

    MAX_SHARK_REPRODUCTION_TIME: int = 10
    shark_reproduction_time: int = MAX_SHARK_REPRODUCTION_TIME
    shark_energy: int = 10
    alive: bool = True
    img: str = "🦈"
    
    
    def __init__(self, x, y):
        super().__init__(x, y)
        

    def move(self, grid) -> None:
        '''
            Fonction move:
            On définit les 4 directions, et on les rend aléatoires.
            On parcourt une fois les directions dans une boucle pour vérifier si il y a un poisson 
            a proximité pour le faire passer en priorité et le manger.
            Si il n'y a pas de poisson, on refait une boucle pour choisir une case aléatoire parmis les cases vides.
        
        '''

        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x = (self.position[0] + dx) % len(grid[0])
            new_y = (self.position[1] + dy) % len(grid)
            neighbor = grid[new_y][new_x]

            if isinstance(neighbor, Fish):
                grid[new_y, new_x] = None # pour supprimer le poisson
                self.eat()
                grid[self.position[1]][self.position[0]] = None
                self.reproduce()
                self.position = [new_x, new_y]
                grid[new_y, new_x] = self
                return
        
        for dx, dy in directions:
            new_x = (self.position[0] + dx) % len(grid[0])
            new_y = (self.position[1] + dy) % len(grid)

            if grid[new_y][new_x] is None:
                grid[self.position[1]][self.position[0]] = None
                self.reproduce()
                self.position = [new_x, new_y]
                grid[new_y, new_x] = self
                break

        self.shark_energy -= 1
        if self.shark_energy == 0:
            self.alive = False


    def eat(self) -> None:
       '''
            Fonction eat :
            Lorsque le requin mange, on augmente son énergie
       '''
       self.shark_energy += 3


    def reproduce(self) -> object:  
        """
            Fonction gérant la reproduction des requins
            Lorsque le timer tombe à 0 un nouveau requin naît, et le compteur est réinitialisé

        """        

        self.shark_reproduction_time -= 1
        if self.shark_reproduction_time == 0:    
            self.shark_reproduction_time = self.MAX_SHARK_REPRODUCTION_TIME
            return Shark(x = self.x, y = self.y)
        


