from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.shark import Shark
from entity.clown_fish import ClownFish

class GridView(QWidget):
    """
    Classe gérant l'affichage de la grille et des éléments graphiques.

    Hérite de QWidget afin de permettre le dessin personnalisé de la grille
    et des entités (poissons, requins) via l’événement paintEvent.
    sur la grille.
    """
    def __init__(self, planet,parent =None):
        super().__init__(parent)
        self.planet=planet
        #Calcul et attibut qui permet de rendre dynamique la taill des cellule et la longueur et largeur de la gridview
        rows=self.planet.width
        cols=self.planet.height
        self.cell_width = 1300 // cols
        self.cell_height = 880 // rows
        self.cell_size = min(self.cell_width, self.cell_height)

        self.rows = rows
        self.cols = cols
        
        self.setMinimumSize(
            self.planet.width * self.cell_size,
            self.planet.height * self.cell_size
        )
                
    def paintEvent(self, event)->None:
        """
        Dessine la grille et les entités à l'écran.

        Affiche chaque cellule en fonction de son contenu (vide, poisson, requin).
        Change la couleur de fond selon la matrice `grid`.

        Args:
            event (QPaintEvent): Événement graphique requis par le système de rendu.
        """
        painter = QPainter(self)
        emotesize=int(self.cell_size/2)
        painter.setFont(QFont("Arial",emotesize ))
        for x in range(self.planet.width):
            for y in range(self.planet.height):
                cell_value = self.planet.grid[y][x]
                
                #couleur en fonction du contenue
                if cell_value=="":
                    color = QColor("cyan")
                    img = ""
                elif (cell_value =="ClownFish" or isinstance(cell_value, ClownFish)):
                    color = QColor("blue")
                    img = "🐠"
                elif (cell_value =="shark" or isinstance(cell_value, Shark)):
                    color = QColor("red")
                    img ="🦈"
                else:
                    color = QColor("cyan")
                    img = ""

                # Dessine le carré principal de girdView
                painter.fillRect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                    color,
                )
                #dessine le cadrillage les petite cellule de la grid
                painter.setPen(Qt.white)
                painter.drawRect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                #permet d'afficher les poissons ainsi de centrer les poisson dans les cellules
                painter.drawText(
                    x* self.cell_size,
                    y* self.cell_size,
                    self.cell_size,
                    self.cell_size,
                    Qt.AlignCenter|Qt.AlignTop,
                    img
                )

    def update_grid(self)->None:
        """
        Met à jour l'affichage graphique de la grille.

        Appelée toutes les 3 secondes pour refléter les changements dans la simulation.
        """
        #boucle qui permet la mise a jour des contenue des cellules
        for x in range(self.planet.width):
            for y in range(self.planet.height):
                cell_value = self.planet.grid[y][x]
                
                #couleur en fonction du contenue
                if cell_value=="":
                    color = QColor("cyan")
                    img = ""
                elif (cell_value =="ClownFish" or isinstance(cell_value, ClownFish)):
                    color = QColor("blue")
                    img = "🐠"
                elif (cell_value =="shark" or isinstance(cell_value, Shark)):
                    color = QColor("red")
                    img ="🦈"
                else:
                    color = QColor("cyan")
                    img = ""
                    
        
