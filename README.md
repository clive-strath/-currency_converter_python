# Currency Converter

A simple Python command-line currency converter that uses the FreeCurrencyAPI to get real-time exchange rates.

## Features

- Convert between 10 major currencies: USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, HKD, NZD
- Real-time exchange rates from FreeCurrencyAPI
- Interactive command-line interface
- Error handling for API requests

## Prerequisites

- Python 3.7+
- Virtual environment (recommended)

## Installation

1. Clone or navigate to the project directory:
```bash
cd /home/clive/Documents/-currency_converter_python
```

2. Activate the virtual environment:
```bash
source .venv/bin/activate
```

3. Install required dependencies:
```bash
pip install requests
```

## Usage

Run the currency converter:

```bash
python currency.py
```

Or using the virtual environment directly:
```bash
.venv/bin/python currency.py
```

### Example Interaction

```
Enter the base currency (q to quit): USD
EUR: 0.92
GBP: 0.79
JPY: 149.85
AUD: 1.53
CAD: 1.36
CHF: 0.88
CNY: 7.24
HKD: 7.82
NZD: 1.65

Enter the base currency (q to quit): EUR
USD: 1.09
GBP: 0.86
JPY: 163.12
AUD: 1.67
CAD: 1.48
CHF: 0.96
CNY: 7.88
HKD: 8.51
NZD: 1.80

Enter the base currency (q to quit): q
```

## Supported Currencies

- **USD** - US Dollar
- **EUR** - Euro
- **GBP** - British Pound
- **JPY** - Japanese Yen
- **AUD** - Australian Dollar
- **CAD** - Canadian Dollar
- **CHF** - Swiss Franc
- **CNY** - Chinese Yuan
- **HKD** - Hong Kong Dollar
- **NZD** - New Zealand Dollar

## API Configuration

The application uses FreeCurrencyAPI with a hardcoded API key. To use your own API key:

1. Sign up at [FreeCurrencyAPI](https://freecurrencyapi.com/)
2. Get your API key
3. Update the `API_KEY` variable in `currency.py`:

```python
API_KEY = "your_api_key_here"
```

## Project Structure

```
-currency_converter_python/
├── .venv/                 # Virtual environment
├── .git/                  # Git repository
├── currency.py            # Main application
└── README.md              # This documentation
```

## Code Overview

### Functions

- `convert_currency(base)`: Fetches exchange rates for a given base currency
  - Parameters: `base` (str) - Base currency code
  - Returns: Dictionary of exchange rates or None on error

### Main Loop

The application runs an infinite loop that:
1. Prompts for a base currency
2. Validates the input
3. Fetches exchange rates
4. Displays conversion rates for all other currencies
5. Allows user to quit by entering 'q'

## Error Handling

- Network errors are caught and displayed
- Invalid currency inputs are rejected with a helpful message
- API response errors are handled gracefully

## Dependencies

- `requests`: HTTP library for making API calls

## License

This project is open source. Feel free to modify and distribute.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request
