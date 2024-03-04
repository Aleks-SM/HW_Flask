import requests

response = requests.post('http://127.0.0.1:5001/adverts',
                         json={"title": "adverts_user1", "description": "qweqweqw", "owner": "user1"}
                         )
                         # params={"name": "Jane", "age": "34"},
                         # headers={"token": "some_token"})
print(response.status_code)
print(response.text)



# response = requests.get('http://127.0.0.1:5001/adverts/1')
#
# print(response.status_code)
# print(response.text)

# response = requests.patch('http://127.0.0.1:5001/adverts/1',
#                           json={"title": "change_title", "description": "qweqweqw", "owner": "user2"})
#
# print(response.status_code)
# print(response.text)

# response = requests.delete('http://127.0.0.1:5001/adverts/1')
#
# print(response.status_code)
# print(response.text)