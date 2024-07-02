import requests
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='portfolio_tracker.log', level=logging.ERROR)

# Replace with your Alpha Vantage API key
API_KEY = 'your_alpha_vantage_api_key'

# Portfolio data structure
portfolio = {}

# Function to fetch stock price from Alpha Vantage
def fetch_stock_price(stock_symbol):
    try:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=1min&apikey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        if "Time Series (1min)" in data:
            latest_data = list(data["Time Series (1min)"].values())[0]
            return float(latest_data["1. open"])
        else:
            raise Exception(f"No data found for {stock_symbol}")
    except Exception as e:
        logging.error(f"{datetime.now()} - Error fetching data for {stock_symbol}: {e}")
        return None

# Function to add stock to portfolio
def add_stock(stock_symbol, quantity):
    if stock_symbol in portfolio:
        portfolio[stock_symbol] += quantity
    else:
        portfolio[stock_symbol] = quantity
    print(f"Added {quantity} shares of {stock_symbol} to your portfolio.")

# Function to remove stock from portfolio
def remove_stock(stock_symbol, quantity):
    if stock_symbol in portfolio:
        if portfolio[stock_symbol] > quantity:
            portfolio[stock_symbol] -= quantity
        elif portfolio[stock_symbol] == quantity:
            del portfolio[stock_symbol]
        else:
            print(f"You only have {portfolio[stock_symbol]} shares of {stock_symbol}.")
        print(f"Removed {quantity} shares of {stock_symbol} from your portfolio.")
    else:
        print(f"{stock_symbol} is not in your portfolio.")

# Function to view portfolio
def view_portfolio():
    if portfolio:
        print("Your portfolio:")
        for stock, quantity in portfolio.items():
            print(f"{stock}: {quantity} shares")
    else:
        print("Your portfolio is empty.")

# Function to track portfolio performance
def track_performance():
    total_value = 0.0
    for stock, quantity in portfolio.items():
        price = fetch_stock_price(stock)
        if price is None:
            print(f"Error fetching data for {stock}")
        else:
            total_value += price * quantity
    print(f"Total portfolio value: ${total_value:.2f}")

# Main menu
def main():
    while True:
        print("\n1. Add Stock\n2. Remove Stock\n3. View Portfolio\n4. Track Performance\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            stock_symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            add_stock(stock_symbol, quantity)
        elif choice == '2':
            stock_symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            remove_stock(stock_symbol, quantity)
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            track_performance()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # your code here
    main()