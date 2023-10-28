import requests

response = requests.get("http://127.0.0.1:8000/menu/")
print(response.json())

response = requests.post("http://127.0.0.1:8000/order?item=pizza&quantity=2")