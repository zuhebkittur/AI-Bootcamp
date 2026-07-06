# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)

# import requests
# response = requests.get("https://api.github.com")
# print(response.json())

# import requests
# response = requests.get("https://api.github.com")
# data = response.json()
# print(data["current_user_url"])

# import requests
# response = requests.get("https://api.github.com/users/zuhebkittur")
# data = response.json()
# print(data["public_repos"])

# import requests
# response = requests.get("https://api.github.com/users/zuhebkittur")
# data = response.json()
# print("Username:", data["login"])
# print("Repositories:", data["public_repos"])
# print("Followers:", data["followers"])
# print("Following:", data["following"])
# print("Profile:", data["html_url"])

import requests
response = requests.get("https://api.github.com/users/zuhebkittur")
data = response.json()
print(data.keys())