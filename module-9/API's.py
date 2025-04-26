#Kristopher Kuenning
#4/26/25
#CSD325
#Module 9.2 API's


import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)
print(response.json())