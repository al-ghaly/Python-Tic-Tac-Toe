# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XO\computerDiff.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from com_easy import *
from com_med import *
from com_hard import *


class Ui_Diff(object):

    def setupUiDiff(self, StartWindow):

        self.easyWindow = QtWidgets.QMainWindow()
        self.ui_easy = Ui_EasyWindow()
        self.ui_easy.setupUiEasy(self.easyWindow)

        self.medium_window = QtWidgets.QMainWindow()
        self.ui_med = Ui_MedWindow()
        self.ui_med.setupUiMed(self.medium_window)

        self.hard_window = QtWidgets.QMainWindow()
        self.ui_hard = Ui_HardWindow()
        self.ui_hard.setupUiHard(self.hard_window)

        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(500, 330)
        StartWindow.setMinimumSize(QtCore.QSize(500, 330))
        StartWindow.setMaximumSize(QtCore.QSize(500, 330))
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.med_button = QtWidgets.QPushButton(self.centralwidget)
        self.med_button.setGeometry(QtCore.QRect(180, 140, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.med_button.setFont(font)
        self.med_button.setObjectName("med_button")
        self.easyButton = QtWidgets.QPushButton(self.centralwidget)
        self.easyButton.setGeometry(QtCore.QRect(20, 140, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.easyButton.setFont(font)
        self.easyButton.setObjectName("easyButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 200, 35))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.hard_button = QtWidgets.QPushButton(self.centralwidget)
        self.hard_button.setGeometry(QtCore.QRect(340, 140, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.hard_button.setFont(font)
        self.hard_button.setObjectName("hard_button")
        StartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StartWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        StartWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StartWindow)
        self.statusbar.setObjectName("statusbar")
        StartWindow.setStatusBar(self.statusbar)
        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "StartWindow"))
        self.med_button.setStatusTip(_translate("StartWindow", "play vs  the computer medium mode"))
        self.med_button.setText(_translate("StartWindow", "Medium"))
        self.easyButton.setStatusTip(_translate("StartWindow", "Play vs the computer Easy mode"))
        self.easyButton.setText(_translate("StartWindow", "Easy"))
        self.label.setText(_translate("StartWindow", "Select Mode :"))
        self.hard_button.setStatusTip(_translate("StartWindow", "play vs the computer hard mode"))
        self.hard_button.setText(_translate("StartWindow", "Hard"))
