import pandas as pd
import os
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ---------------------------------------
# 1. Load Dataset
# ---------------------------------------

data = pd.read_csv("dataset/spam.csv")

print("Dataset loaded successfully!")
print("Total records:", len(data))

# Remove missing values
data = data.dropna()

# ---------------------------------------
# 2. Convert Labels
# ---------------------------------------

data["label"] = data["label"].map({
    "ham": 0,
    "spam": 1
})

X = data["message"]
y = data["label"]


# ---------------------------------------
# 3. Split Dataset
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ---------------------------------------
# 4. TF-IDF Vectorization
# ---------------------------------------

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=5000
)

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)


# ---------------------------------------
# 5. Train Naive Bayes Model
# ---------------------------------------

model = MultinomialNB()

model.fit(
    X_train_vectorized,
    y_train
)


# ---------------------------------------
# 6. Prediction
# ---------------------------------------

y_pred = model.predict(X_test_vectorized)


# ---------------------------------------
# 7. Model Evaluation
# ---------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Training Completed!")
print("----------------------------")
print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# ---------------------------------------
# 8. Create Model Folder
# ---------------------------------------

os.makedirs("model", exist_ok=True)


# ---------------------------------------
# 9. Save Model
# ---------------------------------------

with open("model/spam_model.pkl", "wb") as file:
    pickle.dump(model, file)


# ---------------------------------------
# 10. Save Vectorizer
# ---------------------------------------

with open("model/vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)


print("\nModel saved successfully!")
print("Location: model/spam_model.pkl")

print("Vectorizer saved successfully!")
print("Location: model/vectorizer.pkl")