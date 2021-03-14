# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.solveInStrategies = QtWidgets.QPushButton(self.centralwidget)
        self.solveInStrategies.setGeometry(QtCore.QRect(850, 10, 91, 51))
        self.solveInStrategies.setObjectName("solveInStrategies")
        self.log = QtWidgets.QTextEdit(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(950, 10, 151, 331))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.log.setFont(font)
        self.log.setObjectName("log")
        self.reduceBtn = QtWidgets.QPushButton(self.centralwidget)
        self.reduceBtn.setGeometry(QtCore.QRect(850, 70, 91, 23))
        self.reduceBtn.setObjectName("reduceBtn")
        self.rowsBox = QtWidgets.QSpinBox(self.centralwidget)
        self.rowsBox.setGeometry(QtCore.QRect(120, 0, 51, 22))
        self.rowsBox.setObjectName("rowsBox")
        self.columnBox = QtWidgets.QSpinBox(self.centralwidget)
        self.columnBox.setGeometry(QtCore.QRect(310, 0, 51, 22))
        self.columnBox.setObjectName("columnBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 101, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 0, 121, 16))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 831, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setAutoScroll(False)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        self.makeMatrixBtn = QtWidgets.QPushButton(self.centralwidget)
        self.makeMatrixBtn.setGeometry(QtCore.QRect(370, 0, 151, 23))
        self.makeMatrixBtn.setObjectName("makeMatrixBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.loadMenuItem = QtWidgets.QAction(MainWindow)
        self.loadMenuItem.setObjectName("loadMenuItem")
        self.menu.addAction(self.loadMenuItem)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.solveInStrategies.setText(_translate("MainWindow", "Чистые/\n"
"смешанные\n"
"стратегии"))
        self.reduceBtn.setText(_translate("MainWindow", "Редукция"))
        self.label.setText(_translate("MainWindow", "Количество строк"))
        self.label_2.setText(_translate("MainWindow", "Количество столбцов"))
        self.makeMatrixBtn.setText(_translate("MainWindow", "Сформировать таблицу"))
        self.menu.setTitle(_translate("MainWindow", "Файл..."))
        self.loadMenuItem.setText(_translate("MainWindow", "Загрузить"))
