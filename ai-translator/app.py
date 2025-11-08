from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Azure Function URL (replace with your deployed function)
AZURE_FUNCTION_URL = "https://<your-function-app>.azurewebsites.net/api/ai_function"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_text():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'Please enter text'}), 400

    # Call Azure Function
    res = requests.post(AZURE_FUNCTION_URL, json={"text": text})
    if res.status_code != 200:
        return jsonify({'error': 'AI function failed'}), 400

    return jsonify({'result': res.json()})

if __name__ == '__main__':
    app.run(debug=True)
