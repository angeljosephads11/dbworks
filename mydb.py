import mysql.connector
con = mysql.connector.connect(user='root',password='root',host='localhost')
# #         # establish  connection between python code and mysql server
# #         # it returns a  connection object
# print(con)
# c=con.cursor()     #execute sql queries / commands
# #      #c.execute(command)
# c.execute('create database school_db')
# print('database file created')
# con = mysql.connector.connect(user='root',password='root',host='localhost',database='school_db')
# c=con.cursor()
# c.execute('''
# create table students(roll_no int not null primary key,name varchar(20),
# age int,place varchar(20),phone varchar(20),total_mark int)''')
# # print('table created successfully')
# c.execute(''' insert into students(roll_no,name,age,place,phone,total_mark)
# values(101,'arun',11,'ekm','233456789',145),
# (102,'amal',12,'ekm','102334567',140),(103,'anu',11,'tvm','201334567',147),
# (104,'hari',12,'tcr','233459098',144),(105,'manu',11,'ekm','983456789',141)''');
# query="insert into students(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"
# data=(106,'angel',22,'kannur','346789054',155)
# c.execute(query,data)
# con.commit()# to save data permanantly inside db
# # print('data inserted')
# query1='select * from students'
# c.execute(query1)
# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print('record not found')

# read all attributes of a studnet with roll number = roll number entered by user

# number=int(input('enter the roll number'))
# query='select * from students where roll_no=%s'
# data=(number,)
# c.execute(query,data)
# record = c.fetchone()
# if record:
#     print(record)
# else:
#     print('record not found')
#update mark of a  student with roll number = roll number entered by user
# number=int(input('enter the roll number'))
# mark=int(input('enter the mark'))
# query='update students set total_mark=%s where roll_no=%s'
# data=(mark,number)
# c.execute(query,data)
# query="select * from students"
# c.execute(query)
# record=c.fetchall()
# if record:
#     for row in record:
#         print(row)
# else:
#     print("no record found")
# # delete a record with rollnumber = roll number entered by user
# number=int(input('enter the roll number'))
# mark=int(input('enter the mark'))
# query='update students set total_mark=%s where roll_no=%s'
# data=(mark,number)
# c.execute(query,data)
# query="select * from students"
# c.execute(query)
# record=c.fetchall()
# if record:
#     for row in record:
#         print(row)
# else:
#     print("no record found")
# # delete a record with rollnumber = roll number entered by user
# number=int(input('enter the roll number'))
# mark=int(input('enter the mark'))
# query='update students set total_mark=%s where roll_no=%s'
# data=(mark,number)
# c.execute(query,data)
# query="select * from students"
# c.execute(query)
# record=c.fetchall()
# if record:
#     for row in record:
#         print(row)
# else:
#     print("no record found")
#con.commit()
# delete a record with rollnumber = roll number entered by user
# number=int(input('enter the roll number'))
# query='delete from students where roll_no=%s'
# data=(number,)
# c.execute(query, data)
# record=c.fetchone()
# con.commit()
# create a new record  using values entered by user
# number=int(input('enter the roll number'))
# name=input('enter the name')
# age=int(input('enter the age'))
# place= input('enter the place')
# phone = input('enter the phone number')
# total_mark=int(input('enter the total mark'))
# query="insert into students(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"
# data=(number,name,age,place,phone,total_mark)
# c.execute(query,data)
# con.commit()









# Create a database named shop
con = mysql.connector.connect(user='root',password='root',host='localhost',database='Shop')
c=con.cursor()
# print('using the shope database')
# Create a table `Product` with the following fields:
# c.execute('''create table product(product_id int primary key ,name varchar(30),brand varchar(30),category varchar(30),price int,stock int)''')
# con.commit()
#  `product_id` – Primary Key
#  `name`
#  `brand`
#  `category`
#  `price`
#  `stock`
#
# Write a menu-driven Python program using MySQL with the following options:
def insert():
    product_id=int(input('enter the product-id'))
    name=input('enter the name')
    brand=input('enter the brand')
    category=input('enter the category')
    price=int(input('enter the price'))
    stock=int(input('enter the stock number'))
    query='''insert into product(product_id,name,brand,category,price,stock) values(%s,%s,%s,%s,%s,%s)'''
    data=(product_id,name,brand,category,price,stock)
    c.execute(query,data)
    con.commit()
def read():
    query='select * from product'
    c.execute(query,)
    record=c.fetchall()
    if record:
        for row in record:
            print(row)
    else:
        print('no record found')
    con.commit()
def search():
    product_id=int(input('enter the product-id'))
    query='select * from product where product_id=%s'
    data=(product_id,)
    c.execute(query,data)
    record=c.fetchone()
    if record:
        print(record)
    else:
        print('no record found')
    con.commit()
def update():
    stock=int(input('enter the stock number'))
    product_id=int(input('enter the product-id that need to update the stock'))
    query='update product set stock=%s where product_id=%s'
    data=(stock,product_id)
    c.execute(query,data)
    con.commit()
def delete():
    product_id=int(input('entr the product id that need to be deleted'))
    quer='delete from product where product_id=%s'
    data=(product_id,)
    c.execute(quer,data)
    con.commit()
while True:
    print(' click 1 for insert ')
    print('2 for Read all Product details')
    print('3 for Search a Product by product_id')
    print('4 for Update the stock of a Product')
    print('5 fro delete a product record')
    print('6 fro exiting')
    ch=int(input('enter the choice'))

    if ch==1:
        insert()
    elif ch==2:
        read()
    elif ch==3:
        search()
    elif ch==4:
        update()
    elif ch==5:
        delete()
    elif ch==6:
        exit()


# text
# 1. Insert Product details
# 2. Read all Product details
# 3. Search a Product by product_id
# 4. Update the stock of a Product
# 5. Delete a Product record
# 6. Exit