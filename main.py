
from planet import Planet
# from PyQt5 import QtCore
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
from utils.config import *


""" SETTINGS """
"""
    Pour changer les valeurs, aller dans utils/config.py
"""

NB_OF_FISHES = number_of_fishes
NB_OF_SHARKS = number_of_sharks

GRID_ROWS = rows
GRID_COLUMNS = columns



""" GENERATE """

test_world = Planet(width=GRID_COLUMNS, height=GRID_ROWS)
test_world.display_planet()
test_world.random_init_pos(nb_fishes=NB_OF_FISHES, nb_shark=NB_OF_SHARKS)
test_world.run_simulation()



""" AFFICHAGE """

# test de Mainwindows
# app = QApplication(sys.argv)
# main = MainWindow(test_world,GridView,ClownFish,Shark,HistoryWindow)
# main.show()
# sys.exit(app.exec())
# main.update()


