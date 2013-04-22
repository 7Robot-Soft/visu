#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Fichier définissant l'interface générale
"""

import sys


from PyQt4 import QtGui, QtCore

# TODO : nettoyer les import

WINDOW_WIDTH  = 600
WINDOW_HEIGHT = 400

class Interface(QtGui.QMainWindow):
    """
    Interface principale
    """
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        super(QtGui.QMainWindow, self).__init__()
        self.initUI()

    def getAppHandle(self):
        return self.app
        
    def initUI(self):               
        self.setWindowTitle('Visu')    
        self.setGeometry(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
               
        self.plateauView = PlateauView(self)
        self.plateauView.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.setCentralWidget(self.plateauView)
        
        self.robot = self.plateauView.addItemToScene("img/robot.png", 150, 100, 0, 1)
        
        
        self.show()

        

    def moveRotateRobot(self, x, y, theta):
        print ("received", x, y, theta)
        self.plateauView.moveRotate(self.robot, x, y, theta)
        

class Sprite:
    """
    Pour gérer tous les objets avec des images
    Chaque objet a 2 positions : 
        - sa position sur le plateau (self.x, self.y)
        - sa position dans la fenêtre (self.item.x(), self.item.Y())
    """
    def __init__(self, item, x=0, y=0, theta=0, scale=1):
        self.item  = item # contient l'image et la position/rot/size du sprite sur la fenêtre
        self.origPixmap = self.item.pixmap()
        self.x = x # position plateau, pas celle sur la fenêtre resizable
        self.y = y
        self.theta = theta
        self.scale = scale
        self.item.setTransformOriginPoint(QtCore.QPointF(self.origPixmap.width()/2, self.origPixmap.height()/2))
        
    def resize(self, scale):
        self.scale = scale
        self.redraw()
        
    def redraw(self):
        self.item.setScale(self.scale)
        self.item.setX(-self.origPixmap.width()/2+self.scale*self.origPixmap.width()/2+self.x*self.scale)
        self.item.setY(-self.origPixmap.height()/2+self.scale*self.origPixmap.height()/2+self.y*self.scale)
        self.item.setRotation(self.theta)
        
        
    def moveRotate(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
        self.redraw()
        
        
        
    
    
    
class PlateauView(QtGui.QGraphicsView):
    def __init__(self, parent=None):
        """
        Plateau QGraphicsView redimmensionnable
        """
        super(PlateauView, self).__init__(parent)
        self.img_plateau = QtGui.QPixmap('img/plateau.png')
        
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff )
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff )
        
        self.setViewportUpdateMode(QtGui.QGraphicsView.FullViewportUpdate)
        
        self.sprites = []

        self.scene = QtGui.QGraphicsScene()
        backround_item = self.scene.addPixmap(self.img_plateau)
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
        return len(self.sprites)-1

 
    def moveRotate(self, sprite_id, x, y, theta):
        """
        Déplacer un sprite
        @param: sprite_id (int) index du sprite renvoyé par addItemToScene()
        """
        self.sprites[sprite_id].moveRotate(x, y, theta)
	
    def resizeEvent(self, event):
        """
        Callback appellé lors du redimmensionnement de la fenêtre
        """
        super(PlateauView, self).resizeEvent(event)
        
        size = event.size()
        
        self.scene.setSceneRect(0,0,size.width(), size.height())
        scale = min(size.width()/WINDOW_WIDTH, size.height()/WINDOW_HEIGHT)

        for sprite in self.sprites:
            sprite.resize(scale)
