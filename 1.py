from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Path to your WebDriver executable
driver_path = 'path/to/chromedriver'  # Replace with the actual path

# URL for Tesla revenue data
url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'

# Initialize the WebDriver
driver = webdriver.Chrome(driver_path)
driver.get(url)

# Get page source after JavaScript has rendered the content
page_source = driver.page_source

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

# Close the WebDriver
driver.quit()

# Find all tables
tables = soup.find_all('table')

# Print the number of tables found
print(f"Number of tables found: {len(tables)}")

# Assuming the second table is correct based on inspection
if len(tables) > 1:
    revenue_table = tables[1]
    
    # Extract the data into a dataframe
    tesla_revenue = pd.read_html(str(revenue_table))[0]

    # Clean the data
    tesla_revenue = tesla_revenue.rename(columns={'Tesla Quarterly Revenue(Millions of US $)': 'Date', 'Tesla Quarterly Revenue(Millions of US $).1': 'Revenue'})
    tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace(',', '').astype(int)
    
    # Display the last five rows
    print(tesla_revenue.tail())
else:
    print("Revenue table not found")
