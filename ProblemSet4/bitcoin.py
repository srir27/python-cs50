import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=") # add the correct api key
    # print(response.status_code)
    response = response.json()
    amount = float(response["data"]["priceUsd"]) * n
    print(f"${amount:,.4f}")


except requests.RequestException:
    sys.exit("End")