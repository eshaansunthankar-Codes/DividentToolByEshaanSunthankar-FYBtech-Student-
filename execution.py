import yfinance as yf
import matplotlib.pyplot as plt


choice = input("What would you like to do? \n1. View dividend history of a stock\n2. Compare dividends of two stocks\nEnter 1 or 2: ")


sample_stocks = {
    "RELIANCE.NS": "Reliance Industries",
    "TCS.NS": "Tata Consultancy Services",
    "INFY.NS": "Infosys",
    "HDFCBANK.NS": "HDFC Bank",
    "ITC.NS": "ITC Ltd",
    "SBIN.NS": "State Bank of India",
    "TATAMOTORS.NS": "Tata Motors",
    "HINDUNILVR.NS": "Hindustan Unilever"
}

print("\nHere are some example stock symbols you can use:")
for symbol, name in sample_stocks.items():
    print(f"{symbol} - {name}")


if choice == "1":
    stock = input("\nEnter the stock symbol (Ending with .NS): ")
    data = yf.Ticker(stock)
    dividends = data.dividends
    filtered = dividends[dividends.index >= "2020-01-01"]

    if filtered.empty:
        print("No dividends found for this stock in the last 5 years.")
    else:
        print(f"\nAverage dividend of {stock}: ₹{filtered.mean():.2f}")
        plt.figure(figsize=(10, 5))
        plt.plot(filtered.index, filtered.values, label=stock)
        plt.title(f"{stock} Dividend History (2020 till Present)")
        plt.xlabel("Date")
        plt.ylabel("Dividend Amount")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()


elif choice == "2":
    stock1 = input("\nEnter the first stock symbol (Ending with .NS): ")
    stock2 = input("Enter the second stock symbol (Ending with .NS): ")

    data1 = yf.Ticker(stock1)
    data2 = yf.Ticker(stock2)

    div1 = data1.dividends[data1.dividends.index >= "2020-01-01"]
    div2 = data2.dividends[data2.dividends.index >= "2020-01-01"]

    if div1.empty or div2.empty:
        print("One or both companies have no dividend data in the last 5 years. Please try using another company.")
    else:
        print(f"\nAverage dividend for {stock1}: ₹{div1.mean():.2f}")
        print(f"Average dividend for {stock2}: ₹{div2.mean():.2f}")

        plt.figure(figsize=(10, 5))
        plt.plot(div1.index, div1.values, label=stock1)
        plt.plot(div2.index, div2.values, label=stock2)
        plt.title("Dividend Comparison")
        plt.xlabel("Date")
        plt.ylabel("Dividend Amount")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

else:
    print("Invalid choice. Please enter 1 or 2.")
