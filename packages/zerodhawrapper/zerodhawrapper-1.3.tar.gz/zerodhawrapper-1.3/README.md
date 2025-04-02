# Zerodha Wrapper

A Python wrapper for the Zerodha API that simplifies interaction with Zerodha's trading platform.

## Features

- Easy authentication with Zerodha
- Automated login with TOTP support
- Simplified order placement and position management
- Functions for retrieving market data
- Support for futures and options trading
- Historical data retrieval
- Margin checking utilities

## Installation

```bash
pip install zerodhawrapper
```

## Configuration

1. Create a `key.json` file with your API credentials:
```json
{
    "api_key": "your_api_key",
    "api_secret": "your_api_secret"
}
```

2. Create a `credentials.json` file with your login credentials:
```json
{
    "username": "your_zerodha_username",
    "password": "your_zerodha_password",
    "totp": "your_totp_secret"
}
```

## Usage

```python
from zerodhawrapper import initialize_kite, send_order, retrieve_positions

# Initialize the Kite connection
kite = initialize_kite()

# Place an order
order_id = send_order(
    kite=kite,
    symbol="INFY",
    quantity=1,
    transaction_type="BUY",
    order_type="MARKET",
    product="CNC"
)

# Get positions
positions = retrieve_positions(kite)
```

### Available Functions

- `login()`: Authenticate with Zerodha
- `initialize_kite()`: Initialize KiteConnect client
- `get_quote(symbol)`: Get quote for a symbol
- `send_order(...)`: Place trading orders
- `retrieve_positions(kite)`: Get current positions
- `get_nifty50_futures_symbols(kite)`: Get Nifty50 futures symbols
- `get_nearest_nifty_fut_price(kite)`: Get nearest Nifty futures price
- `check_available_margin(kite)`: Check available trading margin
- `get_fno_underlyings()`: Get F&O underlying symbols
- `get_historical(...)`: Get historical data
- And many more...

## Development

To contribute to this project:

1. Clone the repository
2. Install development dependencies: `pip install -e .`
3. Make your changes
4. Submit a pull request

## License

MIT License 