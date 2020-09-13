from main.model import User

def add_user(u_Data):

    # adding user to the user table
    # args- u_Data: a dictionary having user details via form
    
    insertUser=User(u_Data)
    insertUser.save(force_insert=True)


# importing the requests library 
import requests 
import json
  
# api-endpoint 
URL = "https://localhost:3000/showProduct"
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 

userData=json.loads(data)

# adding a new user to table users
add_user(userData)