from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QTime
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.shark import Shark
from entity.clown_fish import ClownFish
from utils.config import *
from utils.data_manager import save_results

class MainWindow(QMainWindow):
    def __init__(self,planet,GridView,Clownfish,Shark,HistoryWindow):
        super().__init__()
        self.planet = planet
        #definition de la fenetre
        self.setWindowTitle("Wator")
        self.resize(1600, 1200)
        
        #bolean pour les statuts de la simulation et la sauvegarde d'historie
        self.isactiveworld=True
        self.save_simulation=True
        self.history_window=HistoryWindow
        
        # QTimer pour contrôler le cycle de simulation (Chronon)
        self.sim_timer =QTimer(self)
        self.sim_timer.setInterval(cycle_time) # modif dans utils/config.py
        self.sim_timer.timeout.connect(self.update_simulation)
        self.sim_timer.start()
        #timer de la l'application
        self.start_time = QTime(0, 0, 0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # update every 1 sec

        # === Widget central ===
        central_widget:QWidget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal horizontal 
        main_layout:QHBoxLayout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Gridview (85%) taille de la fenetre
        self.grid_view = GridView(planet) 
        self.clownfish=Clownfish
        self.shark=Shark
        main_layout.addWidget(self.grid_view, stretch=85)

        # control pannel
        control_panel = QVBoxLayout()
        
        #time label
        self.timer_label = QLabel('', self)
        
        #boutton reset
        btn_reset=QPushButton("Reset", self)
        btn_reset.setFont(QFont('Arial', 16)) 
        btn_reset.clicked.connect(self.restart)
        
        #boutton start/pause
        btn_start_pause=QPushButton("Start / pause", self)
        btn_start_pause.setFont(QFont('Arial', 16)) 
        btn_start_pause.clicked.connect(self.retake)
        
        #boutton quitter
        self.quit_button = QPushButton("Quitter", self)
        self.quit_button.setFont(QFont('Arial', 16)) 
        self.quit_button.clicked.connect(self.quitter)
        
        #boutton historique
        self.history_button = QPushButton("Historique", self)
        self.history_button.setFont(QFont('Arial', 16)) 
        self.history_button.clicked.connect(self.open_history_window)
        
        #ajout des bouttons et text(label) dans la 
        control_panel.addWidget(self.timer_label)
        control_panel.addWidget(btn_reset)
        control_panel.addWidget(btn_start_pause)
        control_panel.addWidget(self.quit_button)
        control_panel.addWidget(self.history_button)
        
        #font et police d'écriture
        self.chronon = QLabel(f"Chronon : {self.planet.chronon}")
        self.shark = QLabel("Shark")
        self.clownfish = QLabel("clownfish")
        self.chronon.setFont(QFont('Arial', 20)) 
        self.shark.setFont(QFont('Arial', 20)) 
        self.clownfish.setFont(QFont('Arial', 20)) 
        #ajout dans la widget control_panel
        control_panel.addWidget(self.chronon)
        control_panel.addWidget(self.shark)
        control_panel.addWidget(self.clownfish)

        #ajout du widget control_panel dans le layout de la main window
        main_layout.addLayout(control_panel)
        
        # Espace extensible pour bien placer les éléments en haut
        control_panel.addStretch()
        
        # Encapsuler dans un widget
        control_widget = QWidget()
        control_widget.setLayout(control_panel)
        #espace boutton et label 15% taille de la fenetre
        main_layout.addWidget(control_widget, stretch=15)
        
    #  methode qui relance l'application
    def restart(self)->None:
        """
        Redémarre proprement la simulation.

        Cette méthode permet de gérer la réinitialisation du programme sans provoquer de plantage,
        notamment lorsqu’on relance la simulation alors qu’elle est en cours.
        """
        QtCore.QCoreApplication.quit()
        status:str = QtCore.QProcess.startDetached(sys.executable, sys.argv)

    #  methode qui mets en pause
    def retake(self)->None:
        """
        Met en pause ou relance la simulation et le timer.

        Si la simulation est en cours, elle est mise en pause.
        Si elle est en pause, elle reprend.
        """
        if self.timer.isActive():
            self.timer.stop()
            self.isactiveworld=False
        else:
            self.timer.start()
            self.isactiveworld=True
            
    def update_timer(self)->None:
        """
        Met à jour le compteur de temps (chronon).
        """
        self.start_time = self.start_time.addSecs(1)
        self.timer_label.setFont(QFont('Arial', 16))
        self.timer_label.setText(f'execution time:  {self.start_time.toString("h")}:{self.start_time.toString("m")}:{self.start_time.toString("s")}')
        
    def update_simulation(self)->None:
        """
        Met à jour la simulation à chaque chronon.

        Met à jour la grille, les poissons, les étiquettes d’information
        ainsi que le compteur de chronon affiché.
        """
        # chronons max modifiables dans utils/config.py condition de fin de simulation
        if(self.planet.chronon>=max_chronons) or (len(self.planet.fishes) ==0) or (len(self.planet.sharks) ==0):
            self.timer.stop()
            if self.save_simulation: 
                self.save_simulation=False
                save_results(self.planet.chronon,len(self.planet.fishes),len(self.planet.sharks))
            return
        
        if(self.isactiveworld):
            num_fishclown:int = 0  # Remise à zéro pour recompter à chaque cycle
            num_shark:int = 0
            
            self.planet.run_simulation()
            #double boucle qui permet de compter le nombre de poisson et de requin
            for row in range(len(self.planet.grid)):
                for col in range(len(self.planet.grid[row])):
                    cell=self.planet.grid[row][col]
                    if(isinstance(cell,ClownFish)):
                        num_fishclown=num_fishclown+1
                    if(isinstance(cell,Shark)):
                        num_shark=num_shark+1
            self.chronon.setText(f'Chronon : {self.planet.chronon}')  # rafraîchir nombre chronon
            self.shark.setText(f'Shark : {num_shark}') # rafraîchir nombre requin
            self.clownfish.setText(f'Clownfish : {num_fishclown}') # rafraîchir nombre poisson
            self.grid_view.repaint()
            
    def open_history_window(self)-> None:
        """
            Ouvre la fenêtre d'historique de simulation passée.

            Cette méthode crée une instance de la classe HistoryWindow et l'affiche.
            Elle est appelée lorsque l'utilisateur clique sur le bouton "Historique".
            La fenêtre d'historique affichera les données de simulation passée chargées à partir
            du fichier CSV history_wator_groupe1.csv.

            Returns:
                None
        """
        self.history_window_instance=self.history_window()
        if self.history_window_instance.isVisible():
            self.history_window_instance.close()
        else:
            self.history_window_instance.move(self.x() + 100, self.y() + 100)
            self.history_window_instance.resize(self.width() - 150, self.height() - 150 )
            self.history_window_instance.show()
        
    def quitter(self):
        self.history_window_instance= self.history_window()
        if self.history_window_instance.isVisible():
            self.history_window_instance.close()
            
        self.close()
        
    def closeEvent(self,event)->None:
        """
        Gère la fermeture propre de la fenêtre principale.

        Cette méthode appelle la méthode de sortie personnalisée
        pour éviter les erreurs lors de la fermeture avec la croix.
        """
        self.quitter()
