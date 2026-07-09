import requests

url = "https://httpbin.org/headers"

headers = {
    "User-Agent": "Zuheb-AI-Bootcamp"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())