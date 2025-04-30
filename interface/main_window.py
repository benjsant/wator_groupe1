from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #definition de la fenetre
        self.setWindowTitle("Wator")
        self.setGeometry(100, 100, 1200, 1000)
        #texte 
        chronon = QLabel("Chronon",self)
        chronon.setGeometry(40, 20, 100, 40)
        shark = QLabel("Shark",self)
        shark.setGeometry(100, 20, 100, 40)
        fish = QLabel("Fish",self)
        fish.setGeometry(150, 20, 100, 40)
        # Création du bouton
        #boutton reset
        reset=QPushButton("Reset", self)
        reset.setGeometry(850, 20, 100, 40)
        reset.clicked.connect(self.restart)
        #boutton 
        start_pause=QPushButton("Start_pause", self)
        start_pause.setGeometry(950, 20, 100, 40)
        start_pause.clicked.connect(self.retake)
        #boutton quitter
        self.quit_button = QPushButton("Quitter", self)
        self.quit_button.setGeometry(1050, 20, 100, 40)  # x, y, largeur, hauteur

        # Connexion du clic à l'action de quitter
        self.quit_button.clicked.connect(self.close)
        
    
     # action method
    def restart(self):
 
        # printing pressed
        print("restart")
        
    def retake(self):
 
        # printing pressed
        print("retake")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())