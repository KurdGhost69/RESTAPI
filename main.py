
from model import GPT2PPL
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app, origins='*')
    
# initialize the model
model = GPT2PPL()

sentence = "String"

@app.route('/api/predict', methods=['POST', 'OPTIONS'])
def predict():
    # add the following line to handle OPTIONS requests
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    


    # get the input sentence from the request
    sentence = request.json['sentence']

    # Define the DeepL API endpoint and parameters
    deepl_endpoint = "https://api-free.deepl.com/v2/translate"
    deepl_params = {
        "text": sentence,
        "source_lang": "sv",
        "target_lang": "en",
        "auth_key": "aa4b9c49-2510-37c5-3a95-51e61b8ac513:fx"
    }

    # Send the translation request to the DeepL API
    deepl_response = requests.post(deepl_endpoint, data=deepl_params).json()

    # Extract the translated text from the DeepL API response
    translated_text = deepl_response["translations"][0]["text"]

    
    # generate the output using the model
    output = model(translated_text)

    print(output)

    print("Hello World")
    
    # return the output as a JSON response
    return jsonify({'output': output})

if __name__ == '__main__':
    # start the Flask application
    app.run(debug=True,port=5000,host="0.0.0.0")
