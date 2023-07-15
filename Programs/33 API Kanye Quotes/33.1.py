import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response)

data = response.json()

print(data)

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

print(latitude)
print(longitude)
