from connection import connection
import mysql.connector
class maintains:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,id,bookid):
        self.id=id
        self.bookid=bookid
    def addmaintains(librarianid,bookid):
        try:
         sql="INSERT INTO maintains (librarianid,bookid)Values(%s,%s)"
         values=(librarianid,bookid,)
         maintains.mycursor.execute(sql,values)
         maintains.connection.commit()

         return ("Operation is completed successfully")
        except mysql.connector.IntegrityError:


            return ("Error librarian ID or book ID is wrong")



    @staticmethod
    def showmallaintains():
        maintains.mycursor.execute('Select * From maintains')
        result = maintains.mycursor.fetchall()

        return result






