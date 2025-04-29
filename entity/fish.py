import random
    
class Fish: 
    def __init__(self, reproduction_time :int, x :int, y :int):
        self.reproduction_time = reproduction_time
        self.chronon = 0 
        self.x = x
        self.y = y

    def move(self, grid):
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
    
    def reproduce(self): 
        """
                Vérifie si le poisson peut se reproduire en fonction de son temps de reproduction. 
                Si le poisson a atteint son temps de reproduction, un nouvel objet Fish est créé 
                à la même position. Sinon, la méthode retourne None.

                Returns:
                    Fish or None: Un nouvel objet Fish si le poisson peut se reproduire, 
                                sinon None.
        """
        if self.chronon >= self.reproduction_time:
            self.reproduction_time = 0
            return Fish(self.x, self.y, self.reproduction_time)
        else :
            return None
        
    def chronon_one_turn(self): 
        self.chronon += 1