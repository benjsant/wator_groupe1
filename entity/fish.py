class Fish:
    """
        Classe mère de Shark et ClownFish représentant les entités de façon générale
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, grid):
        raise NotImplementedError("La méthode move doit être définie dans les sous-classes.")

    def reproduce(self):
        raise NotImplementedError("La méthode reproduce doit être définie dans les sous-classes.")