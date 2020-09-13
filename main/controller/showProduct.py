from  main.model import Products
# importing the requests library 
import requests 
import json
from nltk.stem import PorterStemmer

ps=PorterStemmer()

# displaying products according to filter - price, popularity , datetime
# arg- filter ( the condition by which items are sorted)
# filter by price, popularity, datetime

def show_product(search_item):

    root=ps.stem(search_item)
    showProduct=Products.objects.filter(p_name__istartswith=root)

# filtering items searched ( shorProduct)

def filter_product(showProduct,filter):

    if(filter=="price"):
        col="cost"
    elif(filter=="popularity"):
        col=""
    elif(filter=="datetime"):
        col="reg_date"

    # sorting products according to filter
    showProduct_wFilter=showProduct.objects.all.group_by(col)
    return showProduct_wFilter


# getting data from the product page
  
# api-endpoint 
URL = "https://localhost:3000/"
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 
