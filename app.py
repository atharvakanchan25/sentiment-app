from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained sentiment model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return "🎉 Sentiment Analysis API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if 'text' not in data:
        return jsonify({'error': 'Missing "text" field in JSON body'}), 400

    text = data['text']
    prediction = model.predict([text])[0]

    return jsonify({
        'input_text': text,
        'predicted_sentiment': prediction
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

