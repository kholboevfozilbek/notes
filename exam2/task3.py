import pandas as pd

# Load the data
df = pd.read_csv('covid_19_clean.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Filter the data for June 1, 2020
df_june_1 = df[df['Date'] == '2020-06-01']

# Find the total number of deaths on June 1, 2020
total_deaths = df_june_1['Deaths'].sum()
print(f"Total deaths on June 1, 2020: {total_deaths}")

# Calculate the mean confirmed cases on June 1, 2020
mean_confirmed = df_june_1['Confirmed'].mean()

# Find the Western Pacific countries with confirmed cases greater than the mean
western_pacific_countries = df_june_1[(df_june_1['WHO Region'] == 'Western Pacific') & (df_june_1['Confirmed'] > mean_confirmed)]['Country/Region'].unique()

print("Western Pacific countries with confirmed cases greater than the mean on June 1, 2020:")
for country in western_pacific_countries:
    print(country)