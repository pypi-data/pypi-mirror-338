from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
PORT = os.environ.get('PORT', 3000)

# Configuration
BASE_URL = 'https://prod.adiona.ai/api/v1'

headers = {
    'Content-Type': 'application/json',
}

# Hotel Search API
@app.route('/hotel/search', methods=['POST'])
def hotel_search():
    try:
        data = request.get_json()
        location = data.get('location')
        check_in = data.get('checkIn')
        check_out = data.get('checkOut')
        rooms = data.get('rooms')

        response = requests.post(
            f"{BASE_URL}/hotel/search",
            json={
                'location': location,
                'checkIn': check_in,
                'checkOut': check_out,
                'rooms': rooms,
            },
            headers=headers
        )

        return jsonify(response.json()), response.status_code
    except Exception as error:
        return jsonify({
            'success': False,
            'message': str(error),
            'details': getattr(error.response, 'json', lambda: {})()
        }), getattr(error.response, 'status_code', 500)

# Hotel Info API
@app.route('/hotel/<hotel_id>/info', methods=['GET'])
def hotel_info(hotel_id):
    try:
        response = requests.get(
            f"{BASE_URL}/hotel/{hotel_id}/info",
            headers=headers
        )
        return jsonify(response.json()), response.status_code
    except Exception as error:
        return jsonify({
            'success': False,
            'message': str(error),
            'details': getattr(error.response, 'json', lambda: {})()
        }), getattr(error.response, 'status_code', 500)

# Location Search API
@app.route('/location/search', methods=['GET'])
def location_search():
    try:
        query = request.args.get('query')
        response = requests.get(
            f"{BASE_URL}/location/search",
            headers=headers,
            params={'query': query}
        )
        return jsonify(response.json()), response.status_code
    except Exception as error:
        return jsonify({
            'success': False,
            'message': str(error),
            'details': getattr(error.response, 'json', lambda: {})()
        }), getattr(error.response, 'status_code', 500)

if __name__ == '__main__':
    app.run(port=PORT)
