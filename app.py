from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_stock():
    ticker = request.args.get('ticker')
    if ticker:
        # Make request to Tiingo API
        api_key = '3830cd0f21f53453ffe972d210f56fa2c4d6fdef'  # Replace with your Tiingo API key
        response = requests.get(f'https://api.tiingo.com/tiingo/daily/{ticker}/prices?token={api_key}')
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'Failed to fetch stock data from Tiingo API.'}), 500
    else:
        return jsonify({'error': 'No ticker symbol provided.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
