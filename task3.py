import pandas as pd

# Work with file covid_19_clean.csv

# Read the CSV file
data = pd.read_csv('covid_19_clean.csv')

# Filter the data for June 1, 2020
filtered_data = data[data['Date'] == '2020-06-01']

# Calculate the total number of deaths
total_deaths = filtered_data['Deaths'].sum()

# Print the result
print("Total number of deaths on June 1, 2020:", total_deaths)


# Filter the data for Western Pacific countries
western_pacific_data = filtered_data[filtered_data['WHO Region'] == 'Western Pacific']

# Calculate the mean value of confirmed cases in all countries on June 1, 2020
mean_confirmed_cases = data[data['Date'] == '2020-06-01']['Confirmed'].mean()

# Filter the Western Pacific countries with confirmed cases larger than the mean value
result = western_pacific_data[western_pacific_data['Confirmed'] > mean_confirmed_cases]

# Print the result
print("Western Pacific countries with confirmed cases larger than the mean value on June 1, 2020:")
print(result)