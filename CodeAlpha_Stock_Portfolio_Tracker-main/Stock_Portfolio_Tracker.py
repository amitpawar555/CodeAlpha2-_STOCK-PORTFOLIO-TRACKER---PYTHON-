import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            current_data = yf.Ticker(symbol).history(period='1d')
            current_price = current_data['Close'].iloc[-1]
            total_cost = self.stocks[symbol]['quantity'] * self.stocks[symbol]['average_price']
            total_cost += quantity * current_price
            total_quantity = self.stocks[symbol]['quantity'] + quantity
            self.stocks[symbol]['average_price'] = total_cost / total_quantity
            self.stocks[symbol]['quantity'] = total_quantity
        else:
            current_data = yf.Ticker(symbol).history(period='1d')
            current_price = current_data['Close'].iloc[-1]
            self.stocks[symbol] = {'quantity': quantity, 'average_price': current_price}

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if quantity >= self.stocks[symbol]['quantity']:
                del self.stocks[symbol]
            else:
                self.stocks[symbol]['quantity'] -= quantity
        else:
            print(f"Error: Stock {symbol} not found in the portfolio.")

    def update_portfolio(self):
        for symbol in self.stocks:
            current_data = yf.Ticker(symbol).history(period='1d')
            current_price = current_data['Close'].iloc[-1]
            self.stocks[symbol]['average_price'] = current_price

    def display_portfolio(self):
        print("Stock Portfolio:")
        for symbol, data in self.stocks.items():
            print(f"{symbol}: Quantity - {data['quantity']}, Average Price - {data['average_price']:.2f}")

def main():
    portfolio = StockPortfolio()

    while True:
        print("\n1. Add Stock\n2. Remove Stock\n3. Display Portfolio\n4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity to remove: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            portfolio.update_portfolio()
            portfolio.display_portfolio()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
