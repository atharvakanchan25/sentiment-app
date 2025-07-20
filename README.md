# 💬 Sentiment Analysis Web App (with Docker & CI/CD)

This is a simple yet powerful Sentiment Analysis Web App that predicts whether a given text expresses a **Positive** or **Negative** sentiment using a machine learning model.

Built with:
- 🧠 Logistic Regression (Scikit-learn)
- 🌐 Flask REST API
- 🐳 Docker
- 🔁 GitHub Actions CI/CD
- ☁️ Deployed with Render

---

## 🚀 Live Demo

🌍 **Try it here**: [https://sentiment-app.onrender.com/predict](https://sentiment-app.onrender.com)

Use **Postman** or `curl` to make a POST request like this:

### Request
```json
{
  "text": "I really love this app!"
}
