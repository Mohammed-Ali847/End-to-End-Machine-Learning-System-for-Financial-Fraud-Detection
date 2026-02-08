🧠 Credit Card Fraud Detection System

Machine Learning End-to-End Project

📌 Project Overview

This project presents an end-to-end machine learning system for detecting fraudulent credit card transactions.
It demonstrates the full machine learning lifecycle, including data preprocessing, model training, evaluation, and deployment as a web-based application with a graphical user interface (GUI).

The project focuses on applying machine learning techniques to a real-world financial problem, namely credit card fraud detection.

🎯 Project Objectives

Build a complete Machine Learning Pipeline

Train and compare multiple ML models

Evaluate models using suitable performance metrics

Deploy the best-performing model as a web application

Provide an interactive GUI for real-time predictions

📊 Dataset

Dataset: Credit Card Fraud Detection

Characteristics: Large-scale and highly imbalanced dataset

Features:

Time, Amount

V1 to V28 (PCA-transformed features)

Target Variable:

Class

0 → Legitimate transaction

1 → Fraudulent transaction

Stratified sampling was used to preserve class distribution during data splitting.

⚙️ Machine Learning Pipeline

The following steps were applied:

Data loading and exploration

Data preprocessing and cleaning

Stratified train-test split

Feature scaling using StandardScaler

Model training using Pipeline

Model evaluation and comparison

Model selection and saving

Deployment using FastAPI

🤖 Models Used

Two models were trained and compared:

Logistic Regression

XGBoost Classifier

The final model was selected based on evaluation metrics suitable for imbalanced data.

📈 Model Evaluation

The models were evaluated using the following metrics:

Precision

Recall

F1-score

ROC-AUC

Confusion Matrix

ROC Curve

Precision-Recall Curve

Due to class imbalance, special emphasis was placed on ROC-AUC and Precision-Recall metrics.

✅ XGBoost achieved the best overall performance and was selected for deployment.

🚀 Deployment

The selected model was deployed as a web-based application using FastAPI.

Deployment Features:

RESTful API for predictions

Interactive graphical user interface (GUI)

JSON-based transaction input

Real-time prediction with probability score

🖥️ Graphical User Interface (GUI)

The GUI allows users to:

Input transaction data in JSON format

Submit data to the trained ML model

Receive predictions:

Legit ✅

Fraud ❌

View the probability of fraud for each transaction

▶️ How to Run the Project
1️⃣ Clone the repository
git clone <repository-url>
cd project

2️⃣ Create and activate a virtual environment (optional)
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
uvicorn app.main:app --reload

5️⃣ Open the browser
http://127.0.0.1:8000

📂 Project Structure
project/
│
├── data/
│   └── creditcard.csv
│
├── notebooks/
│   ├── data_exploration.ipynb
│   ├── training.ipynb
│   └── evaluation.ipynb
│
├── models/
│   └── best_model.pkl
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
│
├── requirements.txt
└── README.md

👥 Team Members

محمد جميل عبد القادر قايد

جبران صالح علي جبران

حلمي خميس جبران

📌 Notes

This project is developed for academic purposes.

The focus is on real-world applicability, model performance, and clean deployment.

The project demonstrates a complete Machine Learning End-to-End workflow.

🏁 Conclusion

This project illustrates how machine learning models can be effectively applied to detect fraudulent financial transactions by integrating data processing, model evaluation, and deployment into a single interactive system.
