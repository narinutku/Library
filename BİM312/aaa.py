# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(958, 681)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url(:/asa/background-4232859_1280.png);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 5, 501, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.genre = QtWidgets.QPushButton(self.layoutWidget)
        self.genre.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.genre.setObjectName("genre")
        self.horizontalLayout_2.addWidget(self.genre)
        self.name = QtWidgets.QPushButton(self.layoutWidget)
        self.name.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.name.setObjectName("name")
        self.horizontalLayout_2.addWidget(self.name)
        self.author = QtWidgets.QPushButton(self.layoutWidget)
        self.author.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.author.setObjectName("author")
        self.horizontalLayout_2.addWidget(self.author)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(5, 140, 921, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(520, 20, 401, 111))
        self.pushButton_6.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(310, 20, 171, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.barrow_id = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.barrow_id.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.barrow_id.setObjectName("barrow_id")
        self.verticalLayout_3.addWidget(self.barrow_id)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.barrow_bookid = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.barrow_bookid.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.barrow_bookid.setObjectName("barrow_bookid")
        self.verticalLayout_3.addWidget(self.barrow_bookid)
        self.button_barrow = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_barrow.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.button_barrow.setObjectName("button_barrow")
        self.verticalLayout_3.addWidget(self.button_barrow)
        self.button_return = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_return.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.button_return.setObjectName("button_return")
        self.verticalLayout_3.addWidget(self.button_return)
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(140, 380, 721, 111))
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 10, 361, 431))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.lineEdit_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_name.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout_4.addWidget(self.lineEdit_name)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.lineEdit_mail = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_mail.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_mail.setObjectName("lineEdit_mail")
        self.verticalLayout_4.addWidget(self.lineEdit_mail)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.lineEdit_phone = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_phone.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.verticalLayout_4.addWidget(self.lineEdit_phone)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.lineEdit_address = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_address.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.verticalLayout_4.addWidget(self.lineEdit_address)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.dateEdit = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        self.dateEdit.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_4.addWidget(self.dateEdit)
        self.pushButton_register = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_register.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_register.setObjectName("pushButton_register")
        self.verticalLayout_4.addWidget(self.pushButton_register)
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(510, 50, 391, 281))
        self.label_18.setStyleSheet("   \n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 45, 251, 211))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_11.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_12.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_5.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 10, 471, 81))
        self.pushButton_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(20, 260, 251, 121))
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(430, 100, 471, 261))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_5)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(80, 90, 173, 171))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_17.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_6.addWidget(self.label_17)
        self.lineEdit_libd = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_libd.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_libd.setObjectName("lineEdit_libd")
        self.verticalLayout_6.addWidget(self.lineEdit_libd)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_16.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_6.addWidget(self.lineEdit_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.label_15 = QtWidgets.QLabel(self.tab_5)
        self.label_15.setGeometry(QtCore.QRect(80, 60, 171, 21))
        self.label_15.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(530, 60, 391, 301))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget_3)
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setGeometry(QtCore.QRect(70, 280, 361, 81))
        self.label_13.setStyleSheet("  \n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Search Book"))
        self.pushButton_4.setText(_translate("MainWindow", "ByID"))
        self.genre.setText(_translate("MainWindow", "ByGenre"))
        self.name.setText(_translate("MainWindow", "ByName"))
        self.author.setText(_translate("MainWindow", "ByAuthor"))
        self.pushButton_6.setText(_translate("MainWindow", "SHOW ALL BOOKS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Search Book"))
        self.label_3.setText(_translate("MainWindow", "Please Enter"))
        self.label_4.setText(_translate("MainWindow", "Your ID"))
        self.label_5.setText(_translate("MainWindow", "Book Id"))
        self.button_barrow.setText(_translate("MainWindow", "Barrow"))
        self.button_return.setText(_translate("MainWindow", "Return"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p/></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Barrow/Return Book"))
        self.label_6.setText(_translate("MainWindow", "Full Name"))
        self.label_7.setText(_translate("MainWindow", "E Mail"))
        self.label_8.setText(_translate("MainWindow", "Phone Number"))
        self.label_10.setText(_translate("MainWindow", "Address"))
        self.label_9.setText(_translate("MainWindow", "Date of Birth"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy.MM.d"))
        self.pushButton_register.setText(_translate("MainWindow", "Register"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Register"))
        self.label_11.setText(_translate("MainWindow", "Reason"))
        self.label_12.setText(_translate("MainWindow", "Condition"))
        self.pushButton.setText(_translate("MainWindow", "ADD REPORT"))
        self.pushButton_2.setText(_translate("MainWindow", "GET ALL REPORTS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Reports"))
        self.label_17.setText(_translate("MainWindow", "Librarian ID"))
        self.label_16.setText(_translate("MainWindow", "Book ID"))
        self.pushButton_3.setText(_translate("MainWindow", "Enter"))
        self.label_15.setText(_translate("MainWindow", "Add New"))
        self.pushButton_5.setText(_translate("MainWindow", "Show All of Them"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Maintains"))
import resource
