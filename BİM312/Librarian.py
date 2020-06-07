from  connection import connection
import mysql.connector
from datetime import datetime
from Member import Member
from Reports import Reports
from maintains import maintains
from Keeps import Keeps
class Librarian:
    connection = connection
    mycursor = connection.cursor()
    Member=Member
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone

    def addmember(name,address,phone,email,birtdate):


        Member.registermember(name,address,phone,email,birtdate)
        return "Congratulations,you have registered successfully."
    def addReport(reason,condition):
        Reports.addreport(reason,condition)
        return "Report is added "
    def addmaintains(librarianid,bookid):
        maintains.addmaintains(librarianid,bookid)


#Librarian.addmember("Onur","Adana","123456789","123456@gmail.com",datetime(1999,8,14))
#Member.getallmembers()
#Librarian.addReport("Ur harm bodsdsdok","bad")
#Reports.getallReports()
#maintains.showmallaintains()
#Keeps.getkeepsreport()
#Keeps.keepsReport(14,1)
#Librarian.addmaintains(1,35)