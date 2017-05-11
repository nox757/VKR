# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
from sklearn.externals import joblib
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 380, 711, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 41, 711, 181))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(140, 280, 271, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 340, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 290, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(260, 230, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 290, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 290, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.clearDialog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Меню открытия файла
        self.action = QtWidgets.QAction(QIcon('Open.png'), 'Open', MainWindow)
        self.action.setShortcut('Ctrl+O')
        self.action.setObjectName("action")
        self.action.triggered.connect(self.openfile)

        #Меню сохранения файла
        self.action_2 = QtWidgets.QAction(QIcon('save.png'), 'Save', MainWindow)
        self.action_2.setShortcut('Ctrl+S')
        self.action_2.setObjectName("action_2")
        self.action_2.triggered.connect(self.savefile)

        # Меню отменить ввод
        self.action_3 = QtWidgets.QAction(QIcon('undo.png'), 'Undo', MainWindow)
        self.action_3.setShortcut('Ctrl+Z')
        self.action_3.setObjectName("action_3")
        self.action_3.triggered.connect(self.undoDialog)

        # Меню повторить ввод
        self.action_4 = QtWidgets.QAction(QIcon('redo.png'), 'Redo', MainWindow)
        self.action_3.setShortcut('Ctrl+Y')
        self.action_4.setObjectName("action_4")
        self.action_4.triggered.connect(self.redoDialog)

        # Меню очистить
        self.action_10 = QtWidgets.QAction(QIcon('Clear.png'), 'Clear', MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_10.triggered.connect(self.clearDialog)

        # Меню вырезать
        self.action_12 = QtWidgets.QAction(QIcon('Cut.png'), 'Cut', MainWindow)
        self.action_12.setShortcut('Ctrl+X')
        self.action_12.setObjectName("action_12")
        self.action_12.triggered.connect(self.cutDialog)

        # Меню копировать
        self.action_13 = QtWidgets.QAction(QIcon('copy.png'), 'Copy', MainWindow)
        self.action_13.setShortcut('Ctrl+C')
        self.action_13.setObjectName("action_13")
        self.action_13.triggered.connect(self.copyDialog)

        # Меню вставить
        self.action_14 = QtWidgets.QAction(QIcon('Paste.png'), 'Copy', MainWindow)
        self.action_14.setShortcut('Ctrl+V')
        self.action_14.setObjectName("action_14")
        self.action_14.triggered.connect(self.pasteDialog)

        # Меню помощь
        self.action_15 = QtWidgets.QAction(QIcon('Help.png'), 'Help', MainWindow)
        self.action_15.setObjectName("action_15")
        self.action_15.triggered.connect(self.helpDialog)

        # Меню о программе
        self.action_17 = QtWidgets.QAction(QIcon('about.png'), 'About', MainWindow)
        self.action_17.setObjectName("action_17")
        self.action_17.triggered.connect(self.aboutDialog)

        # Меню выход из программы
        self.action_18 = QtWidgets.QAction(QIcon('exit.png'), 'Exit', MainWindow)
        self.action_18.setShortcut('Ctrl+E')
        self.action_18.setObjectName("action_18")
        self.action_18.triggered.connect(MainWindow.close)

        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_18)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_10)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_12)
        self.menu_2.addAction(self.action_13)
        self.menu_2.addAction(self.action_14)
        self.menu_4.addAction(self.action_15)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.action_17)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.clf = joblib.load('Test_model.pkl')

        self.commandLinkButton.clicked.connect(self.kodgrnti)

        self.pushButton.clicked.connect(self.test)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Программа по подбору кода ГРНТИ"))
        self.label.setText(_translate("MainWindow", "Вставте текст: "))
        self.label_2.setText(_translate("MainWindow", "Журнал:"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.commandLinkButton.setText(_translate("MainWindow", "Выделить код ГРНТИ"))
        self.label_3.setText(_translate("MainWindow", "Код ГРНТИ:"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Правка"))
        self.menu_3.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_4.setTitle(_translate("MainWindow", "Справка"))
        self.action.setText(_translate("MainWindow", "Открыть файл"))
        self.action_2.setText(_translate("MainWindow", "Сохранить отчет"))
        self.action_3.setText(_translate("MainWindow", "Отменить ввод"))
        self.action_4.setText(_translate("MainWindow", "Повторить ввод"))
        self.action_10.setText(_translate("MainWindow", "Очистить"))
        self.action_12.setText(_translate("MainWindow", "Вырезать"))
        self.action_13.setText(_translate("MainWindow", "Копировать"))
        self.action_14.setText(_translate("MainWindow", "Вставить"))
        self.action_15.setText(_translate("MainWindow", "Помощь"))
        self.action_17.setText(_translate("MainWindow", "О программе"))
        self.action_18.setText(_translate("MainWindow", "Выход"))

    def openfile(self):
        filename = QFileDialog.getOpenFileName()[0]
        f = open(filename, 'r')
        data = f.read()
       # data = filename
        f.close()
        self.textEdit.setText(data)

    def savefile(self):
        filename = QFileDialog.getSaveFileName(MainWindow)
        f = open(filename, 'w')
        data = self.textBrowser.toPlainText()
        f.write(data)
        f.close()

    def undoDialog(self):
        self.textEdit.undo()

    def redoDialog(self):
        self.textEdit.redo()

    def clearDialog(self):
        self.textEdit.clear()
        self.textBrowser.clear()

    def cutDialog(self):
        self.textEdit.cut()

    def copyDialog(self):
        self.textEdit.copy()

    def pasteDialog(self):
        self.textEdit.paste()

    def helpDialog(self):
        QtWidgets.QMessageBox.aboutQt(MainWindow)

    def aboutDialog(self):
        QtWidgets.QMessageBox.about(MainWindow, "О программе", "Разработчики: 3 человека")

    def test(self):
        data = self.textEdit.toPlainText()
        self.textBrowser.setText(data)

    def kodgrnti(self):
        data = self.textEdit.toPlainText()
        kod = self.clf.predict(data)
        self.textBrowser_2.setText(kod)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    pal = MainWindow.palette()
    pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QBrush(QtGui.QPixmap("fon.jpg")))
    MainWindow.setPalette(pal)
    MainWindow.setWindowIcon(QIcon('_jpg.png'))
    MainWindow.show()
    sys.exit(app.exec_())