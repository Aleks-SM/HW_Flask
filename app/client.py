import requests

response = requests.post('http://127.0.0.1:5000/adverts',
                         json={"name": "user_1", "password": "1234"},
                         params={"name": "Jane", "age": "34"},
                         headers={"token": "some_token"})
print(response.status_code)
print(response.text)