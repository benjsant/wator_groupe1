from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from grid_view import GridView
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QTime
from planet import Planet

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class MainWindow(QMainWindow):
    def __init__(self,planet):
        super().__init__()
        self.planet = planet
        #definition de la fenetre
        self.setWindowTitle("Wator")
        self.resize(1200, 800)
        self.isactive=True
        
        # QTimer pour contrôler le cycle de simulation (Chronon)
        self.sim_timer =QTimer(self)
        self.sim_timer.setInterval(3000) #3 sec
        self.sim_timer.timeout.connect(self.update_simulation)
        self.sim_timer.start()
        #timer de la l'application
        self.start_time = QTime(0, 0, 0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # update every 1 sec
        
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
        
        #time label
        self.timer_label = QLabel('', self)
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
        
        control_panel.addWidget(self.timer_label)
        control_panel.addWidget(btn_reset)
        control_panel.addWidget(btn_start_pause)
        control_panel.addWidget(self.quit_button)
        
        
        self.chronon = QLabel(f"Chronon : {self.planet.chronon}")
        self.shark = QLabel("Shark")
        self.fish = QLabel("Fish")
        self.chronon.setFont(QFont('Arial', 20)) 
        self.shark.setFont(QFont('Arial', 20)) 
        self.fish.setFont(QFont('Arial', 20)) 
        control_panel.addWidget(self.chronon)
        control_panel.addWidget(self.shark)
        control_panel.addWidget(self.fish)

        main_layout.addLayout(control_panel)
        
        # Espace extensible en bas pour bien placer les éléments en haut
        control_panel.addStretch()
        
        # Encapsuler dans un widget
        control_widget = QWidget()
        control_widget.setLayout(control_panel)
        main_layout.addWidget(control_widget, stretch=15)
        
    #  methode qui relance l'application
    def restart(self)->None:
        QtCore.QCoreApplication.quit()
        status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
        print(status)

    #  methode qui mets en pause
    def retake(self)->None:
        if self.timer.isActive():
            print(self.timer.isActive())
            self.timer.stop()
        else:
            self.timer.start()
            print(self.timer.isActive())
            
    def update_timer(self):
        #mise a jour du temps
        self.start_time = self.start_time.addSecs(1)
        self.timer_label.setFont(QFont('Arial', 16))
        self.timer_label.setText(f'execution time:  {self.start_time.toString("h")}:{self.start_time.toString("m")}:{self.start_time.toString("s")}')
        
    def update_simulation(self):
        self.planet.update()
        self.chronon.setText(f'Chronon : {self.planet.chronon}')  # ou rafraîchir une vue
        
if __name__ == '__main__':
    from planet import Planet
    planet = Planet(20,20)
    planet.grid[10][5]="fish"
    planet.grid[10][4]="shark"
    app = QApplication(sys.argv)
    main = MainWindow(planet)
    main.show()
    sys.exit(app.exec())