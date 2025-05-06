from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.shark import Shark
from entity.fish import Fish
from entity.clown_fish import ClownFish

class GridView(QWidget):
    def __init__(self, planet,cell_size=40,parent =None):
        super().__init__(parent)
        self.planet =planet
        self.cell_size= cell_size
        
        self.setMinimumSize(
            self.planet.width * self.cell_size,
            self.planet.height * self.cell_size
        )
        
        
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setFont(QFont("Arial", self.cell_size-20))
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

         # Dessine le carré
                painter.fillRect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                    color,
                )
                painter.setPen(Qt.white)
                painter.drawRect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                painter.drawText(
                    x* self.cell_size,
                    y* self.cell_size,
                    self.cell_size,
                    self.cell_size,
                    Qt.AlignCenter|Qt.AlignTop,
                    img
                )

    def update_grid(self):
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
                    
        
