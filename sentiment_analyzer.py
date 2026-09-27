import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


# Load dataset
data = pd.read_csv("data/student_feedback.csv")

# Input and target
X = data["feedback"]
y = data["sentiment"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create NLP + Machine Learning pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, predictions)

print("=" * 50)
print("AI STUDENT FEEDBACK SENTIMENT ANALYZER")
print("=" * 50)

print(f"\nModel Accuracy: {accuracy:.2%}")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Interactive prediction
print("\nEnter student feedback to analyze.")
print("Type 'exit' to stop.")

while True:
    feedback = input("\nFeedback: ")

    if feedback.lower() == "exit":
        print("Program ended.")
        break

    prediction = model.predict([feedback])[0]

    print(f"Predicted Sentiment: {prediction}")