import mysql.connector
class VehicleListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(user='root',password='root',host='localhost',database='motor_v')
        print(self.connection)
        self.cursor=self.connection.cursor()
        print('connection established')
    def list(self):
        query='select* from vehicle'
        self.cursor.execute(query)
        record=self.cursor.fetchall()
        if record:
            for row in record:
                print(row)
        else:
            print('no record found')
    def create(self,brand,model,type,price,year):
        query='insert into vehicle(brand,model,type,price,year)values(%s,%s,%s,%s,%s)'
        data=(brand,model,type,price,year)
        self.cursor.execute(query,data)
        self.connection.commit()
        print('the data is inserted successfully')
    def retrieve(self,id):
        query='select* from vehicle where id=%s'
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            print(record)
        else:
            print('no record found')
    def update(self,brand,model,type,price,year,id):
        query='update vehicle set brand=%s,model=%s,type=%s,price=%s,year=%s where id=%s'
        data=(brand,model,type,price,year,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print('the data is updated successfully')
        else:
            print('no record found')
    def delete(self,id):
        query='delete from vehicle where id=%s'
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print('the rocord in that id is deleted successfully')
        else:
            print('no record found')
obj=VehicleListCreateRetrieveUpdateDelete()
# obj.list()
# obj.create('porche','911','petrol',2000000,2019)
# obj.retrieve(3)
# obj.update('kia','windsor','deseil',20000000,2004,2)
obj.delete(2)
