'''
Authors: Dominic Fate, Jagger Hastings, Yoselyn Rafael, Luke Skar, Xavier Younger
Creation Date: 10/17/2024
Description: A basic game program that runs in PyQt5
Name: Main.py
'''

from map import *
from combat import *
from Project_GUI import *
from PyQt5 import QtCore, QtWidgets, QtGui
import sys

if __name__ == "__main__":
    dungeon = LevelMap(1)  # Create the map object
    myPlayer = player(map_obj=dungeon, max_health=1000, current_health=1000, attack=200,defense=100, location=dungeon.player_position)  # Create the player and link to the mapls

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    print(myPlayer)

    ui.player = myPlayer  # Pass the player object to the GUI
    ui.GUImap = dungeon # Pass map obj to GUI
    ui.setupUi(MainWindow)

    #Adds starting equipment
    ui.pickup_item(armor(0, "Basic ChestPlate", "body_armor"))
    ui.pickup_item(armor(0, "Basic Helm", "head_armor"))
    ui.pickup_item(armor(0, "No Glove", "left_gauntlet"))
    ui.pickup_item(armor(0, "No Glove", "right_gauntlet"))
    ui.pickup_item(armor(0, "Basic Grieves", "pants"))
    ui.pickup_item(armor(0, "Basic Boots", "boots"))
    ui.pickup_item(weapon(0, "Basic Sword"))

    MainWindow.show()
    print(ui.player)
    update_player_display(myPlayer,ui)
    sys.exit(app.exec_())



