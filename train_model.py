from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Simple labeled data
texts = [
    "I love this product", 
    "This is bad", 
    "Amazing experience", 
    "Horrible service", 
    "Not good", 
    "Okayish", 
    "Really nice", 
    "I hate it"
]
labels = ["positive", "negative", "positive", "negative", "negative", "neutral", "positive", "negative"]

# Create pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', LogisticRegression())
])

# Train and save model
model.fit(texts, labels)
joblib.dump(model, 'model.pkl')

print("✅ Model trained and saved as model.pkl")

