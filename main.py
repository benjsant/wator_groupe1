from utils.config import *
from interface.grid_view import GridView
from interface.main_window import MainWindow
from interface.history_window import HistoryWindow
from entity.shark import Shark
from entity.clown_fish import ClownFish
from planet import Planet
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

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
#test_world.run_simulation()



""" AFFICHAGE """

app = QApplication(sys.argv)
main = MainWindow(test_world,GridView,ClownFish,Shark,HistoryWindow)
main.show()
sys.exit(app.exec())
main.update()



