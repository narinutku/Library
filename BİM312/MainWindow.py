import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from aaa import Ui_MainWindow
from Reports import Reports
from books import books
from Member import Member
from Librarian import Librarian

from maintains import maintains
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
         super(MyApp,self).__init__()
         self.ui=Ui_MainWindow()
         self.ui.setupUi(self)
         #self.ui.name.toggled.connect(self.onClicked)
        # self.ui.bygenre.toggled.connect(self.onClicked)
         #self.ui.byauthor.toggled.connect(self.onClicked)
         #self.ui.byid.toggled.connect(self.onClicked)
        # self.ui.lineEdit.text()
         #self.ui.genre.click.connect()
         self.ui.name.clicked.connect(self.onClicked)

         self.ui.genre.clicked.connect(self.onClicked)

         self.ui.author.clicked.connect(self.onClicked)
         self.ui.pushButton_4.clicked.connect(self.onClicked)
         self.ui.pushButton_6.clicked.connect(self.onClicked)
         self.ui.button_barrow.clicked.connect(self.onClicked)
         self.ui.pushButton_register.clicked.connect(self.onClicked)
         self.ui.pushButton.clicked.connect(self.onClicked)
         self.ui.pushButton_2.clicked.connect(self.onClicked)
         self.ui.pushButton_3.clicked.connect(self.onClicked)
         self.ui.pushButton_5.clicked.connect(self.onClicked)


         self.ui.button_return.clicked.connect(self.onClicked)
         self.ui.tableWidget.setColumnCount(9)
         self.ui.tableWidget_3.setColumnCount(2)
         self.ui.tableWidget_3.setHorizontalHeaderLabels(("Librarian ID","Book ID"))
         self.ui.tableWidget.setHorizontalHeaderLabels(("ID","Name","Author","Genre","Publishing House","Publication Date","Language","Number of Copies","Availabity"))

         self.ui.tableWidget_2.setColumnCount(3)

         self.ui.tableWidget_2.setHorizontalHeaderLabels(("ID", "Reason", "Condition"))

        # self.ui.searchbook.clicked.connect(self.getSelected)
    def onClicked(self):
        rb = self.sender()

        if rb.text() == "ByName":
            result = books.getbooksbyname((self.ui.lineEdit.text()))
            self.ui.tableWidget.setRowCount(len(result))
            for i in range(len(result)):
                for k in range(9):
                    self.ui.tableWidget.setItem(i, k, QTableWidgetItem(str(result[i][k])))

        elif rb.text() == "ByID":

         result = books.getbooksbyid((self.ui.lineEdit.text()))
         if result is None:
             self.ui.label_2.setText("There is no book belongs to this ID")
         #print(result)

         else:
          print(result)
          self.ui.tableWidget.setRowCount(len(result))


          for k in range(9):
                    self.ui.tableWidget.setItem(0, k, QTableWidgetItem(str(result[k])))

        elif rb.text() == "ByGenre":
           result= books.getbooksbygenre((self.ui.lineEdit.text()))
           self.ui.tableWidget.setRowCount(len(result))



           for i in range(len(result)):
               for k in range (9):
                self.ui.tableWidget.setItem(i, k, QTableWidgetItem(str(result[i][k])))

        elif rb.text()=="Barrow":
            result=Member.barrowbook(self.ui.barrow_id.text(),self.ui.barrow_bookid.text())
            print(result)
            self.ui.label.setText(str(result))
        elif rb.text()=="Return":
            #a=int(self.ui.barrow_id.text())
            #b=int(self.ui.barrow_bookid.text())
                if len(str(self.ui.barrow_id.text()))==0 or len(str(self.ui.barrow_bookid.text()))==0:
                   self.ui.label.setText("Form can not be empty please try again")
                else:
                      result = Member.returnbook(int(self.ui.barrow_id.text()), int(self.ui.barrow_bookid.text()))
                      self.ui.label.setText(str(result))


        elif rb.text()=="Register":
            a = self.ui.dateEdit.date()
            a = a.toPyDate()
            name=self.ui.lineEdit_name.text()



            if (len(str(self.ui.lineEdit_name.text())))==0 or(len(str(self.ui.lineEdit_address.text())))==0 or (len(str(self.ui.lineEdit_mail.text())))==0:
                self.ui.label_18.setText("Form can not be empty please try again")
            else:

             result=Librarian.addmember(self.ui.lineEdit_name.text(),self.ui.lineEdit_address.text(),self.ui.lineEdit_phone.text()
                                       ,self.ui.lineEdit_mail.text(),a)
             id=Member.getmembersbyname(name)
             #print(id)


             self.ui.label_18.setText(str(result)+"\nYOUR ID IS:"+str(id))
        elif rb.text() == "ADD REPORT":
            if len(str(self.ui.lineEdit_2.text()))==0 or len(str(self.ui.lineEdit_3.text()))==0:
                self.ui.label_19.setText("Form can not be empty please try again")
            else:
             result=Librarian.addReport(self.ui.lineEdit_2.text(),self.ui.lineEdit_3.text())
             self.ui.label_19.setText(str(result))
        elif rb.text()=="GET ALL REPORTS":
            result=Reports.getallReports()

            self.ui.tableWidget_2.setRowCount(len(result))
            for i in range(len(result)):
                for k in range(3):
                    self.ui.tableWidget_2.setItem(i, k, QTableWidgetItem(str(result[i][k])))
        elif rb.text()=="Enter":
            if len(str(self.ui.lineEdit_libd.text()))==0 or len(str(self.ui.lineEdit_4.text()))==0:
                self.ui.label_13.setText("Form can not be empty please try again")
            else:
              libıd=int(self.ui.lineEdit_libd.text())
              bookıd=int(self.ui.lineEdit_4.text())
              print(libıd,bookıd)
              result=maintains.addmaintains(libıd,bookıd)


              self.ui.label_13.setText(str(result))

        elif rb.text()=="Show All of Them":
            result = maintains.showmallaintains()

            self.ui.tableWidget_3.setRowCount(len(result))
            for i in range(len(result)):

                for k in range(2):

                    self.ui.tableWidget_3.setItem(i, k, QTableWidgetItem(str(result[i][k])))














        elif rb.text() == "ByAuthor":
            result = books.getbooksbyauthor((self.ui.lineEdit.text()))
            self.ui.tableWidget.setRowCount(len(result))
            for i in range(len(result)):
                for k in range(9):
                    self.ui.tableWidget.setItem(i, k, QTableWidgetItem(str(result[i][k])))
        elif rb.text() == "SHOW ALL BOOKS":

            result = books.getallbooks()

            self.ui.tableWidget.setRowCount(len(result))
            for i in range(len(result)):
                for k in range(9):
                    self.ui.tableWidget.setItem(i, k, QTableWidgetItem(str(result[i][k])))








def app():
    app=QtWidgets.QApplication(sys.argv)
    win=MyApp()
    win.show()
    sys.exit(app.exec_())


app()

