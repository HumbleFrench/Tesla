from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

# URL for GameStop revenue data
url = 'https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue'

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
    gme_revenue = pd.read_html(StringIO(str(revenue_table)))[0]

    # Update column names based on the table structure
    gme_revenue.columns = ['Date', 'Revenue']

    # Remove rows with NaN values in 'Revenue' column
    gme_revenue = gme_revenue.dropna(subset=['Revenue'])

    # Remove commas and dollar signs, then convert to integers
    gme_revenue['Revenue'] = gme_revenue['Revenue'].str.replace(',', '').str.replace('$', '').astype(int)
    
    # Display the last five rows
    print(gme_revenue.tail())
else:
    print("Revenue table not found")
