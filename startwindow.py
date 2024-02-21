# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XO\startwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from computerDiff import *
from Players_mode import *


class Ui_StartWindow(object):

    def setupUi(self, StartWindow):

        self.diff_window = QtWidgets.QMainWindow()
        self.ui_diff = Ui_Diff()
        self.ui_diff.setupUiDiff(self.diff_window)

        self.players_window = QtWidgets.QMainWindow()
        self.ui_players = Ui_Players_Mode()
        self.ui_players.setupUiPlayers(self.players_window)

        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(500, 330)
        StartWindow.setMinimumSize(QtCore.QSize(500, 330))
        StartWindow.setMaximumSize(QtCore.QSize(500, 330))
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ply_mode = QtWidgets.QPushButton(self.centralwidget)
        self.ply_mode.setGeometry(QtCore.QRect(300, 140, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.ply_mode.setFont(font)
        self.ply_mode.setObjectName("ply_mode")
        self.com_mode = QtWidgets.QPushButton(self.centralwidget)
        self.com_mode.setGeometry(QtCore.QRect(30, 140, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.com_mode.setFont(font)
        self.com_mode.setObjectName("com_mode")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 200, 35))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
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
        self.ply_mode.setStatusTip(_translate("StartWindow", "play vs a second player"))
        self.ply_mode.setText(_translate("StartWindow", "2-Players"))
        self.com_mode.setStatusTip(_translate("StartWindow", "Play vs the computer"))
        self.com_mode.setText(_translate("StartWindow", "Computer"))
        self.label.setText(_translate("StartWindow", "Select Mode :"))
