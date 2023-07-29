import requests

#testing addition
url = 'http://127.0.0.1:8000/calculate'
data = {"num1": 7, "num2": 4, "operator": "hello"}
response = requests.post(url, json=data)
print(response.json())

#testing division
url = 'http://127.0.0.1:8000/calculate'
data = {"num1": 8, "num2": 4, "operator": "divide"}
response = requests.post(url, json=data)
print(response.json())

#testing subtraction
url = 'http://127.0.0.1:8000/calculate'
data = {"num1": 8, "num2": 9, "operator": "subtract"}
response = requests.post(url, json=data)
print(response.json())

#testing multiplication
url = 'http://127.0.0.1:8000/calculate'
data = {"num1": 8, "num2": 4, "operator": "multiply"}
response = requests.post(url, json=data)
print(response.json())