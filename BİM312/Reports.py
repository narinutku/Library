from connection import connection
import mysql.connector
from Keeps import Keeps
class Reports:
    connection = connection
    mycursor = connection.cursor()
    def __init__(self,condition,reason):
        self.condition=condition
        self.reason=reason
    def addreport(reason,condition):
        sql="INSERT INTO reports (Reason,ConditionofBooks)Values(%s,%s)"
        values=(reason,condition,)
        Reports.mycursor.execute(sql,values)

        try:

            Reports.connection.commit()
            print(f'{Reports.mycursor.rowcount}  reports saved')
        except mysql.connector.Error as err:
            print('Error', err)
        return "Report is saved"
    @staticmethod
    def getallReports():
         Reports.mycursor.execute('Select * From reports')
         result = Reports.mycursor.fetchall()


         return result
         #for reports in result:
          #  print(f'id:{reports[0]} Reason:{reports[1]} Condition:{reports[2]}')







