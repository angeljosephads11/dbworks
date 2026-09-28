#define a class to perform database operations on book table
#  create a class named book,list,create,retrieve,uodate,delete and define methods list() --> for reading all records
#create() --> for creating a new record
#retrieve() --> for reading a specific record
#update(id,data) --> for updating a specific  record
#delete(id) --> for deleting a specific record


import mysql.connector
class BoookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user='root',password='root',host='localhost',database='library_db'
        )
        print(self.connection)
        self.cursor = self.connection.cursor()
        print('succesfully connected')
    def list(self):
        # reading all records from db taBLE
        query='select * from book'
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            for record in records:
                print(record)
        else:
            print('no reccord found')
    def create(self,title,author,price,page,language):
        query='insert into book(title,author,price,page,language) values(%s,%s,%s,%s,%s)'
        data=(title,author,price,page,language)
        self.cursor.execute(query,data)
        self.connection.commit()
        print('data inserted successfully')
    def retrieve(self,id):
        query='select * from book where id=%s'
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            print(record)
        else:
            print('no record found')
    def update(self,title,author,price,page,language,id):
        query='update book set title=%s,author=%s,price=%s,page=%s,language=%s where id=%s'
        data=(title,author,price,page,language,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print('the record with the given id is updated successfully')
        else:
            print('no record found')
    def delete(self,id):
        pass
        query='delete from book where id=%s'
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print('the record with the given id is deleted successfully')
        else:
            print('no record found')
book_instance=BoookListCreateRetrieveUpdateDelete()
# book_instance.create('ABCD','SAM',500,200,'french')
# book_instance.delete(4)
# book_instance.retrieve(1)
# book_instance.list()
# book_instance.update('ADB','ANGEL',600,250,'GERMANY',1)


