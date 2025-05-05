import sys
import pandas as pd 
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem,QVBoxLayout,QWidget
from PyQt5.QtGui import QFont

CSV_FILE="history_wator_groupe1.csv"

class HistoryWindow(QMainWindow):
    """
            Fenêtre d'historique de simulation.

            Cette classe crée une fenêtre qui affiche l'historique des simulations
            à partir d'un fichier CSV. Elle charge les données et les affiche dans
            un tableau.

            Attributes:
                table_widget (QTableWidget): Le widget de tableau pour afficher les données de l'historique.
    """
    
    # idéee à voir pour plus tard pour lier main_window à history_window: rajouter le fichier csv dans le init   
    # cet idée est pour pouvoir faire un lien avec main_window et le bouton pour lancer la fenetre history qui aura directement le csv 
    # lors de son lancement. 
    def __init__(self):
        """
            Initialise la fenêtre d'historique.

            Définit le titre de la fenêtre, la géométrie, et crée le widget central
            ainsi que le tableau pour afficher les données de l'historique.
        """
        super().__init__()
        self.setWindowTitle("Historique de la simulation")
        # setGeometry(x,y, width, heigth)
        # (x: position horizontale ← → par rapport au coin gauche supérieur de l'écran )
        # (y: position verticale ↑ ↓ par rapport au coin gauche supérieur de l'écran  )
        # (width: largeur de la fenetre en pixel px )
        # (height: hauteur de la fenetre en pixel px )
        self.setGeometry(100,100, 815, 600)

        # Création widget central 
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        #Création layout vertical 
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Création du tableau pour afficher les données 
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        # Définir la police d'écriture en Arial, taille 16
        font = QFont("Arial", 16)
        self.table_widget.setFont(font)


        self.load_history() 

    def load_history(self):
        """
            Charge l'historique des simulations à partir d'un fichier CSV.

            Cette méthode lit le fichier CSV spécifié, charge les données et les
            affiche dans le tableau. Si le fichier n'est pas trouvé, un message
            d'erreur est affiché et le tableau est vidé.

            Raises:
                FileNotFoundError: Si le fichier CSV n'existe pas.
        """
        try: 
            # Chargement des données du fichier CSV
            data_load = pd.read_csv(CSV_FILE)

            # Configuration des colonnes du tableau
            self.table_widget.setColumnCount(5)
            self.table_widget.setHorizontalHeaderLabels(["Date","Heure_Minutes", "Chronons","Poissons restants","Requins restants"])
            self.table_widget.setRowCount(len(data_load))

            # Taille des colonnes 
            self.table_widget.setColumnWidth(0, 100)  # Élargis la colonne "Date" à 100 pixels
            self.table_widget.setColumnWidth(1, 175)  # Élargis la colonne "Heure_Minutes" à 100 pixels
            self.table_widget.setColumnWidth(2, 125)  # Élargis la colonne "Chronons" à 100 pixels
            self.table_widget.setColumnWidth(3, 175)  # Élargis la colonne "Poissons restants" à 150 pixels
            self.table_widget.setColumnWidth(4, 175)  # Élargis la colonne "Requin restants" à 150 pixels

            # Recuperation des valeurs de la DataFrame avec ajout dans les lignes du tableau PyQt
            for index_data_load, row in data_load.iterrows():
                self.table_widget.setItem(index_data_load, 0,QTableWidgetItem(str(row['Date'])))
                self.table_widget.setItem(index_data_load, 1,QTableWidgetItem(str(row['Heure_Minutes'])))
                self.table_widget.setItem(index_data_load, 2,QTableWidgetItem(str(row['Chronons'])))
                self.table_widget.setItem(index_data_load, 3,QTableWidgetItem(str(row['Nombre_Poissons'])))
                self.table_widget.setItem(index_data_load, 4,QTableWidgetItem(str(row['Nombre_Requins'])))

        # Si le fichier n'est pas trouvé, un message d'erreur est affiché et le tableau est vidé.
        except FileNotFoundError:
            print(f"Le fichier {CSV_FILE} n'existe pas, Veuillez d'abord exécuter la simulation .")
            self.table_widget.setRowCount(0) # Il n'y a aucune donnée à afficher 
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    history_window = HistoryWindow()
    history_window.show()
    sys.exit(app.exec_())