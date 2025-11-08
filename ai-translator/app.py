from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Environment variables (set these in Azure → Configuration)
AZURE_TRANSLATOR_KEY = os.getenv("AZURE_TRANSLATOR_KEY")
AZURE_TRANSLATOR_ENDPOINT = os.getenv("AZURE_TRANSLATOR_ENDPOINT")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate_text():
    data = request.get_json()
    text = data.get("text")
    to_lang = data.get("to")

    path = '/translate?api-version=3.0'
    params = f'&to={to_lang}'
    constructed_url = AZURE_TRANSLATOR_ENDPOINT + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': AZURE_TRANSLATOR_KEY,
        'Ocp-Apim-Subscription-Region': 'canadacentral',  # change if your region differs
        'Content-type': 'application/json'
    }
    body = [{'text': text}]

    response = requests.post(constructed_url, headers=headers, json=body)
    result = response.json()
    translated_text = result[0]['translations'][0]['text']
    return jsonify({'translated': translated_text})

if __name__ == "__main__":
    app.run(debug=True)




