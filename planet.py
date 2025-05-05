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
        
                
    def display(self)->None:
        pass
    
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