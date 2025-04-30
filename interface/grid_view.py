from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

class GridView(QWidget):
    def __init__(self, planet,cell_size=20,parent =None):
        super().__init__(parent)
        self.planet =planet
        self.cell_size= cell_size
        
        self.setMinimumSize(
            self.planet.width * self.cell_size,
            self.planet.height * self.cell_size
            
        )
        
    def paintEvent(self, event):
        painter = QPainter(self)
        
        for x in range(self.planet.width):
            for y in range(self.planet.height):
                cell_value = self.planet.grid[x][y]
                
                #couleur en fonction du contenue
                if cell_value=="":
                    color = QColor("white")
                elif cell_value =="fish":
                    color = QColor("blue")
                elif cell_value =="shark":
                    color = QColor("red")
                else:
                    color = QColor("white")

         # Dessine le carré
                painter.fillRect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                    color
                )
                painter.setPen(Qt.black)
                painter.drawRect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )