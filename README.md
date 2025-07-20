# 💬 Sentiment Analysis Web App (with Docker & CI/CD)

This is a simple yet powerful sentiment analysis web app that uses a **Logistic Regression model** to predict whether a given text expresses a **Positive** or **Negative** sentiment.

The app is built with:
- 🧠 Python (Scikit-learn)
- 🌐 Flask API
- 🐳 Docker containerization
- 🔁 CI/CD via GitHub Actions
- ☁️ Deployed live using Render

---

## 🚀 Live Demo

🌍 **Try it here**: [https://sentiment-app.onrender.com/predict](https://sentiment-app.onrender.com/predict)

Use **Postman** or **cURL** to make a `POST` request to the `/predict` endpoint with JSON input:

```json
{
  "text": "I really love this app!"
}
