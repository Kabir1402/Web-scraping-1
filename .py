import requests
from bs4 import BeautifulSoup
import csv

# Define the URL and headers
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
HEADERS = ['Name', 'Distance', 'Mass', 'Radius']

# Create an empty list to store the star's data
star_data = []

# Get the HTML page with requests
response = requests.get(START_URL)

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find all tables with class "wikitable"
tables = soup.find_all('table', {'class': 'wikitable'})

# Loop through each table
for table in tables:
    rows = table.find_all('tr')
    
    # Loop through each row (skipping the header row)
    for row in rows[1:]:
        data = row.find_all('td')
        star_info = [d.text.strip() for d in data]
        
        # Append the data of each row to star_data list
        star_data.append(star_info)

# Write the collected data into a CSV file
with open('stars.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(HEADERS)
    writer.writerows(star_data[:5])  # Writing only the first 5 rows for demonstration
