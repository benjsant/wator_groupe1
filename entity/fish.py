import random
REPRODUCTION_TIME=8 #Temps de reproduction des poissons 

class Fish:
    
    emoji_fish: str = "🐟"

    def __init__(self,x :int, y :int):
        self.chronon_fish = 0 
        self.x = x
        self.y = y

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

        directions=[(0,1), (1,0), (0,-1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_x = (self.position[0] + dx) % len(grid[0])
            new_y = (self.position[1] + dy) % len(grid)

            if grid[new_y][new_x] is None:
                grid[self.position[1]][self.position[0]] = None
                self.position = [new_x, new_y]
                grid[new_y][new_x] = self
                break
    
    def reproduce(self)->object:
        """
                Vérifie si le poisson peut se reproduire en fonction de son temps de reproduction. 
                Si le poisson a atteint son temps de reproduction, un nouvel objet Fish est créé 
                à la même position. Sinon, la méthode retourne None.

                Returns:
                    Fish or None: Un nouvel objet Fish si le poisson peut se reproduire, 
                                sinon None.
        """
        if self.chronon_fish >= REPRODUCTION_TIME:
            self.chronon_fish = 0
            return Fish(self.x, self.y)
        else :
            return None
        
    def chronon_fish_one_turn(self): 
        """_summary_
            Le poisson gagne un chronom 
        """
        self.chronon_fish += 1