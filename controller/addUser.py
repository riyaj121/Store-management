from db.model import Users 

# importing the requests library 
import requests 
import json
  
# api-endpoint 
URL = "http:\\localhost:3000\controller\getData.js"
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 

userData=json.loads(data)

new_User=Users()
# adding a new user to table users
new_User.add_user(
userData.keys()
)