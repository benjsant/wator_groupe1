from entity.fish import Fish
from entity.shark import Shark
from entity.clown_fish import ClownFish
import random
from pprint import pprint # pour afficher ligne par ligne dans la console


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
        fonction qui initialise le monde en 2 dimensions

        Returns:
            list: retourne une variable à 2 dimension. Pour y accéder : grid[y][x]
        """
        """"""
        return [[" " for _ in range(self.width)] for _ in range(self.height)]  
        
                
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
        for y in range(len(self.grid)): # pour chaque ligne
            for x in range(len(self.grid[0])): # pour chaque colonne
                cell = self.grid[y][x]
                if isinstance(cell, Shark):
                    display[y][x] = cell.img
                elif isinstance(cell, ClownFish):
                    display[y][x] = cell.emoji_fish
                else:
                    display[y][x] = " "
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
        self.grid[fish.y][fish.x] = fish


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
        self.grid[shark.y][shark.x] = shark



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
            if self.grid[y][x] == " ":
                return True
            else:
                return False
            


    """ BOUCLE PRINCIPALE """
    def run_simulation(self) :
        """
            Boucle principale de la simulation.
            Les requins sont déplacés, priorité vers les poissons pour les manger, tout en gérant leur reproduction.
            Ensuite déplacement des poissons, avec reproduction.
            
        """

        # Liste prête à accueillir les bébés requins ou poissons
        new_sharks = []
        new_fishes = []
        # On les fait se déplacer, puis on gère leur reproduction
        for shark in self.sharks:
            if shark:
                shark_x = shark.x
                shark_y = shark.y
                shark.move(self.grid)
                # Gestion de la reproduction
                baby_shark = shark.reproduce(x=shark_x, y=shark_y)
                if baby_shark and self.is_valid_position(x = baby_shark.x, y = baby_shark.y):
                    self.grid[baby_shark.y][baby_shark.x] = baby_shark
                    new_sharks.append(baby_shark)
                    
        self.fishes = [fish for fish in self.fishes if fish.alive]
        for fish in self.fishes:
            if fish:
                fish_x = fish.x
                fish_y = fish.y
                fish.move(self.grid)
                baby_fish = fish.reproduce(x = fish_x, y = fish_y)
                if baby_fish and self.is_valid_position(x = baby_fish.x, y = baby_fish.y):
                    self.grid[baby_fish.y][baby_fish.x] = baby_fish
                    new_fishes.append(baby_fish)
        # Ajout des nouveaux poissons / requins
        self.sharks.extend(new_sharks)
        self.fishes.extend(new_fishes)
        # On update pour ne garder que les entités vivantes
        self.sharks = [shark for shark in self.sharks if shark.alive]
        self.fishes = [fish for fish in self.fishes if fish.alive]
        self.chronon+=1