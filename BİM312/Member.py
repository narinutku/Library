from connection import connection
import mysql.connector
from datetime import datetime,timedelta
from books import books
from barrowed import barrowed

class Member:
    connection = connection
    mycursor = connection.cursor()
    books=books
    barrowed=barrowed


    def __init__(self,name,address,phone,email,birtdate):
       self.name=name
       self.address=address
       self.phone=phone
       self.email=email
       self.birtdate=birtdate

    def registermember(name,address,phone,email,birtdate):
        sql=("INSERT INTO member(FullName,Address,PhoneNumber,EMail,DateofBirth) VALUES(%s,%s,%s,%s,%s)" )
        values=(name,address,phone,email,birtdate,)
        Member.mycursor.execute(sql,values)
        try:
            Member.connection.commit()
            print(f'{Member.mycursor.rowcount} record added')
        except mysql.connector.Error as err:
            print('Error', err)

    def getmembersbyname(name):
        sql = "Select * From member where FullName=%s  "
        value = (name,)
        Member.mycursor.execute(sql,value)

        result=Member.mycursor.fetchall()

        return result[0][0]

    def getmembersbyid(id):
        books.mycursor.execute('Select * From Member')
        result = books.mycursor.fetchone()
        return result
    @staticmethod
    def getallmembers():
        Member.mycursor.execute('Select * From Member')
        result = books.mycursor.fetchall()
        for members in result:
            print(members)


    def barrowbook(id,bookid):

        sql = "Select * from member where idMember=%s"
        value = (id,)
        Member.mycursor.execute(sql, value)
        result = Member.mycursor.fetchone()
        resultbook = Member.books.getbooksbyid(bookid)
        try:
         Numberofbooks = int(result[-1])
         availability = resultbook[-1]

         returndate = datetime.today() + \
                     timedelta(days=15)
         record = barrowed(id, bookid, datetime.today(), returndate)
         if Numberofbooks < 3 and availability == 'Yes':
            record.takebook()
            a=(f'{result[1]} you can take {resultbook[1]} \n and you have to return book:{returndate} ')
            return a


         elif Numberofbooks >= 3:
            return ("You have three book you can not take more")
         elif availability == 'No':
            return (f'You can not take {resultbook[1]} it is not availability now')

        except TypeError as err:
            return ('Error your id or book id is wrong please try again')
    def returnbook(id,bookid):

        sql = "Select * from barrowed where bookid=%s "
        value=(bookid,)

        Member.mycursor.execute(sql,value)
        result = Member.mycursor.fetchone()
        print(result)
        try:
         havingbookid = result[1]
         checkid = result[0]
         if havingbookid == bookid and checkid == id:
            barrowed.returnbook(id, bookid)
            return ('Operation is completed successfully your book was returned')
         else:
            print("Book not found please check your filled information")

        except TypeError as err:
            return ('Error your id or book id is wrong please try again')















    #  if result>2:
     #       print("You can not take more books")
      #  else:
       #     sql="UPDATE member SET NumberofHavingBooks = NumberofHavingBooks + 1 WHERE idMember = %s "
        #    value=id

#üye=Member("Utku Narin","Edirne","1234","1234@1234",datetime(1982, 10, 10))
#üye.registermember()


#obj=Member.barrowbook(11,40)
#Member.barrowbook(55,55)
#klasık=books("Dava","albertcamus","classic","YKY",datetime(1982, 10, 10),"turkish",1,"yes")
#klasık.savebook()
#books.savebooks()
#obj=Member.returnbook(1,1)
#print(obj)







