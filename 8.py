import yfinance as yf
import matplotlib.pyplot as plt

# Download GameStop stock data
gme_data = yf.download('GME')

# Reset the index
gme_data.reset_index(inplace=True)

# Function to plot stock data
def make_graph(stock_data, title):
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data['Date'], stock_data['Close'], label='Close Price')
    plt.xlabel('Date')
    plt.ylabel('Close Price USD')
    plt.title(title)
    plt.legend()
    plt.show()

# Plot GameStop Stock Data
make_graph(gme_data, 'GameStop Stock Price')
