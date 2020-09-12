from django.db import models

class Users(models.Model):


    # defining the Table object to access the table users
    Uid=models.AutoField(primary_key=True)
    reg_date=models.DateField(auto_now=True)
    user_fname=models.CharField(20,blank=False)
    user_lname=models.CharField(20,blank=False)
    user_email=models.CharField(50,blank=False)
    user_password=models.CharField(50,blank=False)
    

class Products(models.Model):

    # defining the Table object to access the table products 
            
    Pid=models.AutoField(primary_key=True)
    reg_date=models.DateField(auto_now=True)
    p_name=models.CharField(50,blank=False)
    cost=models.AutoField(blank=False)

    # adding products to the product table
    def add_product(self,p_Data):

        insertProduct=Products(p_Data)
        insertProduct.save(force_insert=True)