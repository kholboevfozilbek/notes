import json

# Load the data from the JSON file
with open("forecast.json", "r") as file:
    data = json.load(file)

# Get the lists of times and temperatures
times = data["hourly"]["time"]
temperatures = data["hourly"]["temperature_2m"]

# Find the index of the desired time
try:
    index = times.index("2024-06-10T04:00")
    # Print the corresponding temperature
    print(f"The temperature at '2024-06-10T04:00' is {temperatures[index]}°C")
except ValueError:
    print("The time '2024-06-10T04:00' was not found in the data.")