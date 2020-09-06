from sqlalchemy import MetaData,create_engine
from sqlalchemy import Table,Column,Integer,DateTime,String
from datetime import datetime
from sqlalchemy import insert
from sqlalchemy import select
metadata=MetaData()

# accessing the db
try:
    engine=create_engine('mysql+pymysql://root:butterscotch@localhost/store',pool_recycle=3600)
except:
    print("Failed to access")

conn=engine.connect()

class Users:

    def __init__(self):

        # defining the Table object to access the table users
        self.users=Table(
            'users',metadata,
            Column('id',Integer,primary_key=True,autoincrement=True),#default=10000),
            Column('reg_date',DateTime(),default=datetime.now),
            Column('user_fname',String(20),nullable=False),
            Column('user_lname',String(20),nullable=False),
            Column('user_email',String(50),nullable=False),
            Column('user_password',String(50),nullable=False),
        )
    
    def add_user(self,u_Data):

        # adding user to the user table
        # args- u_Data: a dictionary having user details via form
        
        insertUser=self.users.insert().values(u_Data)
        res=conn.execute(insertUser)

class Products:

    # defining the Table object to access the table products 
    def __init__(self):
        self.products=Table
        (
            'product',metadata,
            Column('id',Integer(),primary_key=True),
            Column('reg_date',DateTime(),default=datetime.now),
            Column('p_name',String(20),nullable=False),
            Column('cost',Integer(),nullable=False)
        )
    
    # adding products to the product table
    def add_product(self,p_Data):

        insertProduct=self.products.insert().values(p_Data)
        res=conn.execute(insertProduct)

    # displaying products according to filter - price, popularity , datetime
    # arg- filter ( the condition by which items are sorted)
    # filter by price, popularity, datetime
    
    def show_product(self,filter):

        if(filter=="price"):
            col="cost"
        elif(filter=="popularity"):
            col=""
        elif(filter=="datetime"):
            col="reg_date"

        # sorting products according to filter
        showProduct=select([self.products]).group_by(col)
        res=conn.execute(showProduct).fetchall()


metadata.create_all(engine)

