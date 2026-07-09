import requests
url = "https://jsonplaceholder.typicode.com/posts/1"

data = {
    "id": 1,
    "title": "Updated Python",
    "body": "Today I learned PUT requests",
    "userId": 1
}

response= requests.put(url, json=data)
print("Status Code:", response.status_code)
print(response.json())