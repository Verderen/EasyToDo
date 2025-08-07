from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

def get_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    data = response.json()
    return data['price']

@app.route('/')
def index():
    btc_price = get_btc_price()
    return render_template('index.html', btc_price=btc_price)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)