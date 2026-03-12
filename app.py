from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "fca_live_Oip33UnkuiQ7qOEHCf212dadHhcwnHQuFH4ztfV6"
BASE_URL = "https://api.freecurrencyapi.com/v1/latest?apikey=" + API_KEY

CURRENCIES = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "HKD", "NZD"]

def convert_currency(base, target=None, amount=1.0):
    currencies = ",".join(CURRENCIES)
    url=f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    
    try:
        response = requests.get(url)
        data = response.json()
        rates = data["data"]
        
        if target:
            if target in rates:
                return {target: rates[target] * amount}
            else:
                return None
        else:
            return rates
    except Exception as e:
        print("Error occurred:", e)
        return None

@app.route('/')
def index():
    return render_template('index.html', currencies=CURRENCIES)

@app.route('/convert', methods=['POST'])
def convert():
    base_currency = request.form.get('base_currency')
    target_currency = request.form.get('target_currency')
    amount = float(request.form.get('amount', 1.0))
    
    if not base_currency or not target_currency:
        return jsonify({'error': 'Please select both currencies'})
    
    if base_currency == target_currency:
        return jsonify({'error': 'Base and target currencies cannot be the same'})
    
    result = convert_currency(base_currency, target_currency, amount)
    
    if result:
        return jsonify({
            'success': True,
            'base_currency': base_currency,
            'target_currency': target_currency,
            'amount': amount,
            'result': result[target_currency]
        })
    else:
        return jsonify({'error': 'Failed to get exchange rates'})

@app.route('/rates/<base_currency>')
def get_rates(base_currency):
    if base_currency not in CURRENCIES:
        return jsonify({'error': 'Invalid currency'})
    
    rates = convert_currency(base_currency)
    if rates:
        return jsonify({'success': True, 'rates': rates})
    else:
        return jsonify({'error': 'Failed to get exchange rates'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
