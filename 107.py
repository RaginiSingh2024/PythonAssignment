# Requests Module
import requests

response = requests.get("https://api.example.com/data") 
response.raise_for_status() 

data = response.json()
print(data['key1']['value'])