import requests

# response = requests.post('http://127.0.0.1:5000/adverts',
#                          json={"title": "user2", "description": "qweqweqw"}
#                          )
#                          # params={"name": "Jane", "age": "34"},
#                          # headers={"token": "some_token"})
# print(response.status_code)
# print(response.text)

response = requests.post('http://127.0.0.1:5000/users',
                         json={"username": "user1", "password": "qweqweqw", "email": "qq@ya.ru"}
                         )
                         # params={"name": "Jane", "age": "34"},
                         # headers={"token": "some_token"})
print(response.status_code)
print(response.text)

# response = requests.get('http://127.0.0.1:5000/adverts/1')
#
# print(response.status_code)
# print(response.text)

# response = requests.patch('http://127.0.0.1:5000/adverts/1',
#                           json={"title": "change_title", "description": "qweqweqw", "owner": "sdfsdf"})
#
# print(response.status_code)
# print(response.text)