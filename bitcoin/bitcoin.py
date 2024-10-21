import sys
import requests

def main():
    # Check if the user provided a command-line argument
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    # Try to convert the argument to a number (float), this is a function
    # converting a string (text) into a decimal number (float)
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    # Get the current price of Bitcoin from the CoinDesk API
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()  # Convert response to JSON
        bitcoin_price = data['bpi']['USD']['rate_float']  # Get the price in USD
    except requests.RequestException:
        print("Error: Unable to retrieve Bitcoin price.")
        sys.exit(1)

    # Now what we should do is to calculate the total cost
    total_cost = bitcoins * bitcoin_price

    # Print the total cost with commas and four decimal places
    print(f"${total_cost:,.4f}")

# Only run the program if this file is executed directly
if __name__ == "__main__":
    main()