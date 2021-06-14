from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QPainter
from view.viewFinal import *

class gridView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sokoban")
        self.setStyleSheet("background-color:#C3C9C5")
        self.setFixedSize(450,450)
        self.__controller = None
        self.__model = None

    def setModel(self, model):
        self.__model = model

    def getModel(self):
        return self.__model

    def setController(self, controller):
        self.__controller = controller

    def getController(self):
        return self.__controller

    def updateView(self):
        self.update()

    def paintEvent(self,event):
        painter = QPainter(self)
        plateau = self.__model.getPlateau()
        model = self.getModel()
        for i in range(len(plateau)):
            for j in range(len(plateau[i])):
                case = plateau[j][i]
                if (i == model.getPlayer()[0] and j == model.getPlayer()[1]):
                    if(self.__model.getDirection()=="droite"):
                        r = QtCore.QRect(j*50, i*50, 40, 50)
                        image_path = "images/personnage/Fighter_Right.png"
                        pixmap = QPixmap(image_path)
                        pixmap = pixmap.scaled(r.size())
                        painter.drawPixmap(r, pixmap)
                    elif(self.__model.getDirection()=="gauche"):
                        r = QtCore.QRect(j*50, i*50, 40, 50)
                        image_path = "images/personnage/Fighter_Left.png"
                        pixmap = QPixmap(image_path)
                        pixmap = pixmap.scaled(r.size())
                        painter.drawPixmap(r, pixmap)
                    elif (self.__model.getDirection() == "haut"):
                        r = QtCore.QRect(j * 50, i * 50, 40, 50)
                        image_path = "images/personnage/Fighter_Back.png"
                        pixmap = QPixmap(image_path)
                        pixmap = pixmap.scaled(r.size())
                        painter.drawPixmap(r, pixmap)
                    elif (self.__model.getDirection() == "bas"):
                        r = QtCore.QRect(j * 50, i * 50, 40, 50)
                        image_path = "images/personnage/Fighter_Front.png"
                        pixmap = QPixmap(image_path)
                        pixmap = pixmap.scaled(r.size())
                        painter.drawPixmap(r, pixmap)
                if (case == 1):
                    r = QtCore.QRect(i*50,j*50,50,50)
                    im =QtGui.QPixmap("images/mur.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r,im)
                if (case == 2):
                    r = QtCore.QRect(i*50,j*50,50,50)
                    im =QtGui.QPixmap("images/objets/Petite_caisse.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r,im)
                if (case == 3):
                    r = QtCore.QRect(i * 50, j * 50, 50, 50)
                    im = QtGui.QPixmap("images/objets/caisseE.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r, im)
                if (case == 4):
                    r = QtCore.QRect(i * 50, j * 50, 50, 50)
                    im = QtGui.QPixmap("images/objets/etoile.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r, im)
        self.__controller.Victoire()

    def keyPressEvent(self,event):
        value=event.key() - 16777234
        if value == 0:
            if self.__controller.checkG(self.__model.getPlayer()[0], self.__model.getPlayer()[1]):
                self.__model.setDirection("gauche")
                self.__model.updatePlayer([self.__model.getPlayer()[0], self.__model.getPlayer()[1]-1])
                self.__model.addPas()
        elif value == 1:
            if self.__controller.checkH(self.__model.getPlayer()[0], self.__model.getPlayer()[1]):
                self.__model.setDirection("haut")
                self.__model.updatePlayer([self.__model.getPlayer()[0]-1,self.__model.getPlayer()[1]])
                self.__model.addPas()

        elif value == 2:
            if self.__controller.checkD(self.__model.getPlayer()[0],self.__model.getPlayer()[1]):
                self.__model.setDirection("droite")
                self.__model.updatePlayer([self.__model.getPlayer()[0], self.__model.getPlayer()[1]+1])
                self.__model.addPas()

        elif value == 3:
            if self.__controller.checkB(self.__model.getPlayer()[0], self.__model.getPlayer()[1]):
                self.__model.setDirection("bas")
                self.__model.updatePlayer([self.__model.getPlayer()[0]+1, self.__model.getPlayer()[1]])
                self.__model.addPas()


    def updateView(self):
        self.update()
