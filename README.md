# 📧 Email Spam Detection

A Machine Learning and NLP based web application that classifies email messages as **Spam** or **Ham (Not Spam)**.

## 🚀 Overview

This project uses Natural Language Processing (NLP) and Machine Learning techniques to analyze email text and predict whether a message is spam or legitimate.

The application provides a simple web interface where users can enter an email message and instantly get the prediction.

## ✨ Features

* 📩 Spam and Ham email classification
* 🧠 NLP-based text processing
* 🔤 TF-IDF text vectorization
* 🤖 Machine Learning based prediction
* 🌐 Simple Flask web application
* ⚡ Real-time email classification

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **Scikit-learn**
* **Pandas**
* **NumPy**
* **NLTK**
* **HTML**
* **CSS**

## 🔄 Workflow

```text
Email Text
    ↓
Text Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Machine Learning Model
    ↓
Spam / Ham Prediction
```

## 📁 Project Structure

```text
Email_Spam_Detection/
│
├── app.py
├── train_model.py
├── spam.csv
├── spam_model.pkl
├── vectorizer.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Itsjanvi/Email_Spam_Detection.git
cd Email_Spam_Detection
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

Enter an email message and check whether it is classified as **Spam** or **Ham**.

## 🎯 Objective

The main objective of this project is to demonstrate how NLP and Machine Learning can be used for automatic spam email detection.

## 🔮 Future Scope

* Improve model accuracy with larger datasets
* Experiment with different Machine Learning algorithms
* Add advanced NLP techniques
* Deploy the application online
* Support multiple languages

## 👩‍💻 Author

**Janvi**

GitHub: [Itsjanvi](https://github.com/Itsjanvi)

---

⭐ If you find this project useful, consider giving it a star!
