from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

# URL for Tesla revenue data
url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'

# Set up the Chrome WebDriver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
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

# Extract the correct table (second table, index 1)
if len(tables) > 1:
    revenue_table = tables[1]
    
    # Extract the data into a dataframe using StringIO
    tesla_revenue = pd.read_html(StringIO(str(revenue_table)))[0]

    # Print the dataframe to inspect its structure
    print(tesla_revenue.head())
    
    # Update column names based on the table structure
    tesla_revenue.columns = ['Date', 'Revenue']

    # Remove rows with NaN values in 'Revenue' column
    tesla_revenue = tesla_revenue.dropna(subset=['Revenue'])

    # Remove commas and dollar signs, then convert to integers
    tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace(',', '').str.replace('$', '').astype(int)
    
    # Display the last five rows
    print(tesla_revenue.tail())
else:
    print("Revenue table not found")
