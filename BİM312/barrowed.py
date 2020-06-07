from connection import connection
import mysql.connector
from datetime import datetime
from books import books

class barrowed:
    connection = connection
    mycursor = connection.cursor()
    books=books
    def __init__(self,userid,bookid,issuedate,returndate):
        self.userid=userid
        self.bookid=bookid
        self.issuedate=issuedate
        self.returndate=returndate
    def takebook(self):
        sql = "INSERT INTO barrowed(userid,bookid,issuedate,returndate)VALUE(%s,%s,%s,%s)"
        values=(self.userid,self.bookid,self.issuedate,self.returndate,)
        barrowed.mycursor.execute(sql,values)
        userid=self.userid
        bookid=self.bookid

        try:
          barrowed.connection.commit()
          print(f'{barrowed.mycursor.rowcount} book taken')
          books.updatenumberofbook(userid,bookid)


        except mysql.connector.Error as err:
         print('Error', err)


    def returnbook(id,bookid):
        sql="DELETE FROM barrowed where  bookid=%s "
        value=(bookid,)
        barrowed.mycursor.execute(sql,value)
        barrowed.connection.commit()
        sql = " UPDATE Member SET NumberofHavingBooks = NumberofHavingBooks - 1 where idMember=%s "
        sql2 = " UPDATE book SET  Availabity ='Yes' where id=%s "
        value = (id,)
        value2 = (bookid,)
        barrowed.mycursor.execute(sql, value)
        barrowed.mycursor.execute(sql2, value2)

        barrowed.connection.commit()
        print(f'{barrowed.mycursor.rowcount} book was returned')





  #  def registermember(name,address,phone,birtdate):
   #     sql=("INSERT INTO member(FullName,Address,PhoneNumber,EMail,DateofBirth) VALUES(%s,%s,%s,%s,%s)" )
    #    values=(self.name,self.address,self.phone,self.email,self.birtdate,)
      #  Member.mycursor.execute(sql,values)
