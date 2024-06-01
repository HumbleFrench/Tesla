import yfinance as yf

# Download Tesla stock data
tesla_data = yf.download('TSLA')

# Reset the index
tesla_data.reset_index(inplace=True)

# Display the first five rows
print("Tesla Stock Data")
print(tesla_data.head())
