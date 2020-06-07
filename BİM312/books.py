from connection import connection
import mysql.connector
from datetime import datetime

class books:
    connection=connection
    mycursor=connection.cursor()

    def __init__(self,bookname,author,genre,publishinghouse,publicationdate,language,copies,availabity):
        self.bookname=bookname
        self.author=author
        self.genre=genre
        self.publishinghouse=publishinghouse
        self.publicationdate=publicationdate
        self.language=language
        self.copies=copies
        self.availabity=availabity

    def savebook(self):
        sql = ("INSERT INTO book (Name,Author,Genre,PublishingHouse,PublicationDate,Language,NumberofCopies,Availabity) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
        value = (self.bookname, self.author, self.genre,self.publishinghouse,self.publicationdate,self.language,self.copies,self.availabity,)
        books.mycursor.execute(sql, value)
        try:
          books.connection.commit()
          print(f'{books.mycursor.rowcount} record added')
        except mysql.connector.Error as err:
         print('Error', err)
        finally:
         books.connection.close()

    """def getbooksbyname(name):
        sql = "Select * From book where Name=%s"
        value = (name,)
        books.mycursor.execute(sql, value)
        try:
            return books.mycursor.fetchone()
        except mysql.connector.Error as err:
            print('Error', err)
        finally:
            books.connection.close()"""
    def getbooksbyauthor(author):
        sql = "Select * From book where Author like concat('%',%s,'%')  "
        value = (author,)
        books.mycursor.execute(sql,value)
        result = books.mycursor.fetchall()
        return result


    def getbooksbyname(name):
        sql = "Select * From book where name like concat('%',%s,'%')  "
        value = (name,)
        books.mycursor.execute(sql,value)
        result = books.mycursor.fetchall()

        return result
    def getbooksbygenre(genre):
        sql = "Select * From book where genre like concat('%',%s,'%')  "
        value = (genre,)
        books.mycursor.execute(sql,value)
        result=books.mycursor.fetchall()
        return result
        #try:
         #
          #  for book in result:
           #     print(f'Name:{book[1]} Author:{book[2]} Genre:{book[3]} Publishing House:{book[4]} Publishing Date:{book[5]} '
            #          f'Language:{book[6]} Number of Copies:{book[7]} Availabity:{book[8]} ')
       # except mysql.connector.Error as err:
        #    print('Error', err)
        #finally:
         #   books.connection.close()

    def getbooksbyid(id):
            sql="Select * from book where id=%s"
            value = (id,)
            books.mycursor.execute(sql, value)


            result =books.mycursor.fetchone()
            try:
                a=result[0]
                return result
            except TypeError as err:
                return None

    def getbooksnamebyid(id):
            sql="Select * from book where id=%s"
            value = (id,)
            books.mycursor.execute(sql, value)

            result = books.mycursor.fetchone()

            return result
    @staticmethod
    def savebooks(book):
        sql = ("INSERT INTO book (Name,Author,Genre,PublishingHouse,PublicationDate,Language) VALUES (%s,%s,%s,%s,%s,%s)")
        values=book
        books.mycursor.executemany(sql,values)
        try:
          books.connection.commit()
          print(f'{books.mycursor.rowcount} record added')
        except mysql.connector.Error as err:
          print('Error',err)
        finally:
            books.connection.close()

    def deletebooks(Genre):
        sql = "Delete  From book where Genre=%s"
        value = (Genre,)
        books.mycursor.execute(sql, value)

        try:
            books.connection.commit()
            print(f'{books.mycursor.rowcount} record deleted')
        except mysql.connector.Error as err:
            print('Error', err)
        finally:
            books.connection.close()
    def updatenumberofbook(id,bookid):
        sql = " UPDATE Member SET NumberofHavingBooks = NumberofHavingBooks + 1 where idMember=%s "
        sql2=" UPDATE book SET  Availabity ='No' where id=%s "
        value=(id,)
        value2=(bookid,)
        books.mycursor.execute(sql,value)
        books.mycursor.execute(sql2, value2)
        books.connection.commit()







    @staticmethod
    def getallbooks():
        books.mycursor.execute('Select * From book')
        result = books.mycursor.fetchall()

        return result


        #for book in result:
         #print(
          #f'ID:{book[0]} Name:{book[1]} Author:{book[2]} Genre:{book[3]} Publishing House:{book[4]} Publishing Date:({book[5]})'
           #f'Language:{book[6]} Number of Copies:{book[7]} Availabity:{book[8]} ')


#klasık=books("yabancı","albertcamus","classic","YKY",datetime(1982, 10, 10),"turkish",1,"yes")
#klasık.savebook()
kitaplar=[
            ("Şu Çılgın Türkler","Turgut Özakman","Tarih","Bilgi Yayınevi",datetime(2005,7,6),"Turkish"),
            ("Denizlar Altında 20000 Fersah", "Jules Verne", "Classic", "İs Bankası",datetime(2000,2,2),"turkish"),
            ("İnce Mehmed", "Yaşar Kemal", "Türk Klasikleri", "YKY",datetime(2019,1,3),"turkish"),
("İnce Mehmed", "Yaşar Kemal", "Türk Klasikleri", "YKY",datetime(2012,1,3),"turkish"),
("İnce Mehmed 2", "Yaşar Kemal", "Türk Klasikleri", "YKY",datetime(2013,1,3),"turkish"),
("İnce Mehmed 3", "Yaşar Kemal", "Türk Klasikleri", "YKY",datetime(2014,1,3),"turkish"),
("İnce Mehmed 4", "Yaşar Kemal", "Türk Klasikleri", "YKY",datetime(2015,1,3),"turkish"),
("Felatun Bey ile Rakım Efendi", "Ahmet Mithad", "Türk Klasikleri", "İş Bankası",datetime(2019,1,3),"turkish"),
("Efsuncu Baba", "Hüseyin Rahmi Gürpınar", "Türk Klasikleri", "İş Bankası",datetime(2019,1,3),"turkish"),
("Sefiller", "Victor Hugo", "Classic", "İs Bankası",datetime(2000,2,2),"turkish"),
("Notre Dame'ın Kamburu", "Victor Hugo", "Classic", "İs Bankası",datetime(2000,2,2),"turkish"),
("1984", "George Orwell", "Classic", "Can Yayınları",datetime(2010,2,2),"turkish"),
("Nineteen Eighty-four", "George Orwell", "Classic", "Can Yayınları",datetime(2010,2,2),"english"),
("Hayvan Çiftliği", "George Orwell", "Classic", "Can Yayınları",datetime(2010,2,2),"turkish"),
("Paris ve Lonra'da Beş Parasız", "George Orwell", "Classic", "Can Yayınları",datetime(2010,2,2),"turkish"),
("Benjamin Button'ın Tuhaf Hikayesi", "F. Scott Fitzgerald", "American Classic", "İs Bankası",datetime(2018,5,22),"english"),
("Bir Ömür Nasıl Yaşanır ", "İlber Ortaylı", "Tarih", "Kronik Kitap",datetime(2020,3,3),"turkish"),
("Türklerin Tarihi ", "İlber Ortaylı", "Tarih", "Kronik Kitap",datetime(2017,3,3),"turkish"),
("Türklerin Tarihi 2", "İlber Ortaylı", "Tarih", "Kronik Kitap",datetime(2018,3,3),"turkish"),
("Türklerin Altın Çağı ", "İlber Ortaylı", "Tarih", "Kronik Kitap",datetime(2019,3,3),"turkish"),
("İmparatorluğun En Uzun Yüzyılı", "İlber Ortaylı", "Tarih", "Kronik Kitap",datetime(2014,3,3),"turkish"),
            ("Kolera Günlerinde Aşk", "Gabriel García Márquez", "Dram", "Can yayınları",datetime(2015,8,9),"turkish"),
        ]
#books.savebooks(kitaplar)
#deletebooks("American Classic")

#obj=books.getbooksnamebyid(68)
#print(obj)
#obj=books.getallbooks()
#books.getbooksbyauthor("dostoyevski")

