#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from threading import Thread
from time import sleep

from interface import Interface


class VisuCommander(Thread):
    """
    Démo qui donne des ordres de déplacement du robot
    prédéfinis, afin de vérifier que tout marche bien.
    """
    def __init__(self, visu):
        Thread.__init__(self)
        self.visu = visu
 
    def run(self):
        sleep(1)
        # Hum, je suis pas censé faire un appel de fonction
        # qui modifie des objets d'un autre thread (mainloop QT)
        # Apparemment ça marche sans faire de signaux/slots
        self.visu.moveRotateRobot(150.0, 100.0, 0)
        sleep(2)
        for i in range(13*3):
            self.visu.moveRotateRobot(150.0, 100.0, i*30)
            sleep(0.2)
        self.visu.moveRotateRobot(40.0, 40.0, 0.0)
        sleep(1)
        self.visu.moveRotateRobot(60.0, 60.0, 0.0)
        sleep(1)
        self.visu.moveRotateRobot(60.0, 60.0, 45.0)
        sleep(1)
        self.visu.moveRotateRobot(60.0, 60.0, 90.0)
        sleep(1)
        self.visu.moveRotateRobot(60.0, 60.0, 180.0)
        
        
if __name__ == '__main__':
    inter = Interface()
    commander = VisuCommander(inter)
    commander.start()
    sys.exit(inter.getAppHandle().exec_())

            
