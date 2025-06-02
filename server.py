from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/api', methods=['GET'])
def handle_api():
    name = request.args.get('name')
    city = request.args.get('city')
    return jsonify({'message': f'Hello {name} from {city}!'})

if __name__ == '__main__':
    app.run()
