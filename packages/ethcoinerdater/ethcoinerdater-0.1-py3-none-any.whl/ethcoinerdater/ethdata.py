import requests

COINGECKO_API = "https://api.coingecko.com/api/v3/simple/price"

def get_eth_price(currency="usd"):
    """Fetches the latest ETH price in the specified currency (default: USD)."""
    try:
        response = requests.get(COINGECKO_API, params={"ids": "ethereum", "vs_currencies": currency})
        response.raise_for_status()
        return response.json().get("ethereum", {}).get(currency, "Price not found")
    except requests.exceptions.RequestException as e:
        return f"Error fetching price: {e}"

def convert_eth_to_currency(eth_amount, currency="usd"):
    """Converts a given ETH amount to the specified currency."""
    price = get_eth_price(currency)
    if isinstance(price, (int, float)):
        return eth_amount * price
    return price  # Return error message if price fetching failed
