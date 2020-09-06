from sqlalchemy import MetaData,create_engine
from sqlalchemy import Table,Column,Integer,DateTime,String
from datetime import datetime
from sqlalchemy import insert
from sqlalchemy import select
metadata=MetaData()

try:
    engine=create_engine('mysql+pymysql://root:password@localhost/store',pool_recycle=3600)
except:
    print("Failed to access")

conn=engine.connect()

class Users:

    def __init__(self):
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
        
        insertUser=self.users.insert().values(u_Data)
        res=conn.execute(insertUser)

class Products:

    def __init__(self):
        self.products=Table
        (
            'product',metadata,
            Column('id',Integer(),primary_key=True),
            Column('reg_date',DateTime(),default=datetime.now),
            Column('p_name',String(20),nullable=False),
            Column('cost',Integer(),nullable=False)
        )
    
        
    def add_product(self,p_Data):

        insertProduct=self.products.insert().values(p_Data)
        res=conn.execute(insertProduct)

    def show_product(self,filter):
        
        showPdt=select([self.products])
        


metadata.create_all(engine)

