import mysql.connector
con = mysql.connector.connect(user='root',password='root',host='localhost')
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
    c.execute(query)
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
    product_id = int(input('enter the product-id that need to update the stock'))
    stock=int(input('enter the stock number'))
    query='update product set stock=%s where product_id=%s'
    data=(stock,product_id)
    c.execute(query,data)
    query1='select* from product where product_id=%s'
    data=(product_id,)
    c.execute(query1,data)
    record=c.fetchone()
    if record:
        print(record)
    else:
        print('no record found')
    con.commit()
def delete():
    product_id=int(input('enter the product id that need to be deleted'))
    query='delete from product where product_id=%s'
    data=(product_id,)
    c.execute(query,data)
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