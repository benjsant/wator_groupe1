from entity.fish import Fish
import random


class ClownFish(Fish):
    
    REPRODUCTION_TIME = 5 #Temps de reproduction des poissons 
    emoji_fish: str = "🐠"
    alive:bool = True

    def __init__(self,x :int, y :int):
        super().__init__(x, y)
        self.chronon_fish = 0

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

        directions=[(0,1), (1,0), (0,-1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x = (self.x + dx) % len(grid[0])
            new_y = (self.y + dy) % len(grid)

            if grid[new_y][new_x] == " ":
                grid[self.y][self.x] = " "
                self.x = new_x
                self.y = new_y
                grid[new_y][new_x] = self
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