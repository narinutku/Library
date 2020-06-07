from connection import connection
import mysql.connector
class Keeps:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, reportid, librarianid):
        self.reportid= reportid
        self.librarianid = librarianid

    @staticmethod
    def getkeepsreport():
        Keeps.mycursor.execute('Select * From keeps')
        result = Keeps.mycursor.fetchall()
        for i in result:
            print(f'Report ID:{i[0]} Librarian ID:{i[1]} ')
    def keepsReport(reportid,librarianid):
        sql="INSERT INTO keeps (reportno,librarianno)Values(%s,%s)"
        values=(reportid,librarianid)
        Keeps.mycursor.execute(sql,values)
        try:
          Keeps.connection.commit()
          print(f'{Keeps.mycursor.rowcount} record added')
        except mysql.connector.Error as err:
          print('Error',err)
        finally:
            Keeps.connection.close()

