sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# Example Output
# {
# 'What': 4,
# 'is': 2,
# 'the': 3,
# 'Airspeed': 8,
# 'Velocity': 8,
# 'of': 2,
# 'an': 2,
# 'Unladen': 7,
# 'Swallow?': 8
# }

# Write your code below:
list = sentence.split(" ")

result = {item: len(item) for item in list}

print(result)
