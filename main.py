# import requests

# MY_LAT = 20.593684
# MY_LNG = 78.96288

# parameters = {
#   "lat": MY_LAT,
#   "lng": MY_LNG,
# }

# response = requests.get("https://api.sunrise-sunset.org/json",
#                         params=parameters)
# response.raise_for_status()
# data = response.json()
# print(data)

import matplotlib.pyplot as plt

x = [24, 25, 26]
y = [23, 24, 25]

plt.plot(x,y)
plt.show()