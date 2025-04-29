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
        
    def init_grid(self):
        """_summary_
        fonction qui initialize le monde 2 dimension

        Returns:
            list: retourne une variable a 2 dimension pour acceder grid[x][y]
        """
        """"""
        return [[col for col in range(self.height)]for row in range(self.width)]  
                
    def display():
        pass
    
    def update():
        pass
    