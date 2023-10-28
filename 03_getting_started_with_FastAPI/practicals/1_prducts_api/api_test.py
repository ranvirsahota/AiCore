import requests

#response = requests.get("http://127.0.0.1:8000/products/all/")
# OUTPUT
# {
#   '1': {'name': 't-shirt', 'price': 19.99, 'category': 'clothes'},
#   '2': {'name': 'stickers', 'price': 1.99, 'category': 'accessories'},
#   '3': {'name': 'mug', 'price': 9.99, 'category': 'kitchenware'},
#   '4': {'name': 'hoodie', 'price': 29.99, 'category': 'clothes'},
#   '5': {'name': 'cap', 'price': 14.99, 'category': 'accessories'}}

response = requests.get("http://127.0.0.1:8000/products/5")
print(response.json())