class Planet:
    def __init__(self, width:int, height:int):
        """_summary_
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
        return [["" for col in range(self.height)]for row in range(self.width)]  
        
                
    def display(self)->None:
        pass
    
    def update(self)->None:
        self.chronon += 1


    def new_fish(self, fish):
        if not self.is_valid_position(x=self.width, y=self.height):
            return None
        if len(self.fishes) >= (self.width * self.height):
            return None
        self.fishes.append(fish)
        self.grid[fish.x][fish.y] = "🐟" #fish.emoji_fish


    def new_shark(self, shark):
        if not self.is_valid_position(x=self.width, y=self.height):
            return None
        if len(self.sharks) >= (self.width * self.height):
            return None
        self.sharks.append(shark)
        self.grid[shark.x][shark.y] = shark.img


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
            if self.grid[x][y] == None:
                return True
            else:
                return False