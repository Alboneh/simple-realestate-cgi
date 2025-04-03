from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/properties', methods=['GET'])
def get_properties():
    data = [
        {"id": 1, "name": "Luxury Apartment", "price": 500000},
        {"id": 2, "name": "Beach House", "price": 1200000}
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
