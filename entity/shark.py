
class Shark:
    """
    Classe représentant les requins
    Valeurs fixes et communes à toutes les instances de Shark 
    (Utilisation d'attributs de classe et non d'instance car mieux pour l'optimisation de la mémoire)

        - MAX_SHARK_REPRODUCTION_TIME : temps de reproduction par défaut des requins
        - shark_reproduction_time : timer de reproduction des requins (à 0 -> nouveau requin)
        - shark_energy : energie des requins -> à 0 il meurt
        - alive : booléen indiquant si le requin est vivant ou non
        - img : lien de la représentation graphique du requin

    """    

    MAX_SHARK_REPRODUCTION_TIME: int = 10
    shark_reproduction_time: int = MAX_SHARK_REPRODUCTION_TIME
    shark_energy: int = 10
    alive: bool = True
    img: str = "A shark representation"
    
    
    def __init__(self):
        pass

    def move(self):
        self.shark_energy -= 1
        print("The shark moves.", self.shark_energy)
        if self.shark_energy == 0:
            self.alive = False
            print("Le requin est mort.", self.alive, self.shark_energy)


    def reproduce(self):  
        """
        Fonction gérant la reproduction des requins
        Lorsque le timer tombe à 0 un nouveau requin naît, et le compteur est réinitialisé

        """        
        # A ADAPTER AVEC LES CHRONONS

        print("The shark reproduces.")
        self.shark_reproduction_time -= 1
        if self.shark_reproduction_time == 0:
          # création nouveau requin
          self.shark_reproduction_time = self.MAX_SHARK_REPRODUCTION_TIME
        
        print("compteur reproduction : ", self.shark_reproduction_time)


    def eat(self):
       self.shark_energy += 3
       print("The shark eats.", self.shark_energy)

