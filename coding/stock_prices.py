# filename: stock_prices.py
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

def get_stock_price(symbol):
    # Get today's date
    today = datetime.date.today()

    # Get the first day of the year
    start_date = datetime.date(today.year, 1, 1)

    # Download stock price data
    data = yf.download(symbol, start=start_date, end=today)

    # Return the 'Close' column
    return data['Close']

# Get stock prices
nvda = get_stock_price('NVDA')
tsla = get_stock_price('TSLA')

# Plot the data
plt.figure(figsize=(14,7))

plt.plot(nvda.index, nvda, label='NVDA')
plt.plot(tsla.index, tsla, label='TSLA')

plt.title('NVDA vs TSLA YTD Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.show()