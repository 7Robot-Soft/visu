#!/usr/bin/python
# -*- coding: utf-8 -*-

# fichier définissant l'interface générale
import sys

from PyQt4.QtCore import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *

WINDOW_WIDTH  = 600
WINDOW_HEIGHT = 400

class Interface(QtGui.QMainWindow):
    
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        super().__init__()
        self.initUI()

    def getAppHandle(self):
        return self.app
        
    def initUI(self):               

        self.setWindowTitle('Visu')    
        self.setGeometry(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
               
        self.plateauView = PlateauView(self)
        self.plateauView.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.setCentralWidget(self.plateauView)
        
        self.robot = self.plateauView.addItemToScene("im/robot.png", 30, 10, 0, 1)

        self.show()
        
        
class Sprite:
    """
    Pour gérer tous les objets avec des images.
    """
    def __init__(self, item, x=0, y=0, theta=0, scale=1):
        self.item  = item # contient l'image et la position/rot/size du sprite sur la fenêtre
        self.x = x # position plateau, pas celle sur la fenêtre resizable
        self.y = y
        self.theta = 0
        self.scale = scale
        
    def resize(self, scale):
        self.scale = scale
        self.redraw()
        
    def redraw(self):
        self.item.setScale(self.scale)
        self.item.setX(self.x*self.scale)
        self.item.setY(self.y*self.scale)
        self.item.setRotation(self.theta)
        
    def moveRotate(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
        self.redraw()
        
        
        
    
    
    
class PlateauView(QGraphicsView):
    def __init__(self, parent=None):
        """
        QGraphicsView that will show an image scaled to the current widget size
        using events
        """
        super(PlateauView, self).__init__(parent)
        self.im_plateau = QPixmap('im/plateau.png')
        #QMetaObject.connectSlotsByName(self)
        
        self.setHorizontalScrollBarPolicy (Qt.ScrollBarAlwaysOff )
        self.setVerticalScrollBarPolicy (Qt.ScrollBarAlwaysOff )
        
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        
        self.sprites = []

        self.scene = QGraphicsScene()
        backround_item = self.scene.addPixmap(self.im_plateau)
        self.sprites.append(Sprite(backround_item, 0, 0))

        self.setScene(self.scene)
        self.show()
        
    def addItemToScene(self, sprite, x, y, theta, scale):
        """
        @return: sprite_id (int) : index du sprite dans self.sprites
        """
        newItem = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(sprite))
        self.scene.addItem(newItem)
        self.sprites.append(Sprite(newItem, x, y, theta, scale))    
        return len(self.sprites)

 
    def moveRotate(self, sprite_id, x, y, theta):
        self.sprites[sprite_id].moveRotate(x, y, theta)
	
    def resizeEvent(self, event):
        """
        Callback appellé lors du redimmensionnement de la fenêtre
        """
        super(PlateauView, self).resizeEvent(event)
        
        size = event.size()
        scale = min(size.width()/WINDOW_WIDTH, size.height()/WINDOW_HEIGHT)

        for sprite in self.sprites:
            sprite.resize(scale)
            
            
        

        #~ # Si on diminue puis aggrandit l'image d'origine, elle sera floue
        #~ newim_plateau = self.im_plateau
#~ 
        #~ newim_plateau = newim_plateau.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation) # IgnoreAspectRatio/KeepAspectRatio
        #~ #self.centerOn(1, 1)
        #~ #item.setPixmap(newim_plateau)
        
        

        



