import requests
url = "https://jsonplaceholder.typicode.com/posts"

title = input("Enter the title: ")
body= input("Enter the description: ")

data = {
    "title" : title,
    "body"  : body,
    "userId" : 1
}

response = requests.post(url, json=data)
print("\nStatus code:" , response.status_code)

print(response.json())