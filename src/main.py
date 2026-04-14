from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # Handle incoming message
    print(json.dumps(data, indent=4))
    return '', 200

if __name__ == '__main__':
    app.run(port=5000)