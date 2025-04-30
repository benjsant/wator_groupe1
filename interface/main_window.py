from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from grid_view import GridView
import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class MainWindow(QMainWindow):
    def __init__(self,planet):
        super().__init__()
        #definition de la fenetre
        self.setWindowTitle("Wator")
        self.resize(1200, 800)
        
        # === Widget central ===
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal horizontal 
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Grid (85%) 
        self.grid_view = GridView(planet) 
        main_layout.addWidget(self.grid_view, stretch=85)

        # control pannel
        control_panel = QVBoxLayout()
        
        first_layout = QVBoxLayout()
        #boutton reset
        btn_reset=QPushButton("Reset", self)
        btn_reset.setFont(QFont('Arial', 16)) 
        btn_reset.clicked.connect(self.restart)
        
        #boutton 
        btn_start_pause=QPushButton("Start / pause", self)
        btn_start_pause.setFont(QFont('Arial', 16)) 
        btn_start_pause.clicked.connect(self.retake)
        
        #boutton quitter
        self.quit_button = QPushButton("Quitter", self)
        self.quit_button.setFont(QFont('Arial', 16)) 
        self.quit_button.clicked.connect(self.close)
        

        control_panel.addWidget(btn_reset)
        control_panel.addWidget(btn_start_pause)
        control_panel.addWidget(self.quit_button)
        #layout label
        
        
        chronon = QLabel("Chronon")
        shark = QLabel("Shark")
        fish = QLabel("Fish")
        chronon.setFont(QFont('Arial', 20)) 
        shark.setFont(QFont('Arial', 20)) 
        fish.setFont(QFont('Arial', 20)) 
        control_panel.addWidget(chronon)
        control_panel.addWidget(shark)
        control_panel.addWidget(fish)

        main_layout.addLayout(control_panel)
        
        # Espace extensible en bas pour bien placer les éléments en haut
        control_panel.addStretch()
        
        # Encapsuler dans un widget
        control_widget = QWidget()
        control_widget.setLayout(control_panel)
        main_layout.addWidget(control_widget, stretch=15)
        
     # action method
    def restart(self):
 
        # printing pressed
        print("restart")
        
    def retake(self):
 
        # printing pressed
        print("retake")
        
if __name__ == '__main__':
    from planet import Planet
    planet = Planet(30, 30)
    
    app = QApplication(sys.argv)
    main = MainWindow(planet)
    main.show()
    sys.exit(app.exec())