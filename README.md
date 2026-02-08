🧠 Credit Card Fraud Detection System

Machine Learning End-to-End Project

📌 Project Overview

This project presents an end-to-end machine learning system for detecting fraudulent credit card transactions.
The system covers the complete machine learning lifecycle, starting from data preprocessing and model training, to evaluation and deployment as a web-based application.

The project aims to demonstrate how machine learning models can be applied to real-world financial problems, specifically fraud detection.

🎯 Objectives

Build a complete Machine Learning Pipeline

Train and compare multiple ML models

Evaluate models using appropriate performance metrics

Deploy the best-performing model as a web application

Provide an interactive Graphical User Interface (GUI) for predictions

📊 Dataset

Source: Credit Card Fraud Detection Dataset

Size: Large-scale dataset with highly imbalanced classes

Features:

Time, Amount

V1 to V28 (PCA-transformed features)

Target Variable:

Class

0 → Legitimate transaction

1 → Fraudulent transaction

Due to class imbalance, special care was taken during data splitting and evaluation.

⚙️ Machine Learning Pipeline

The following steps were applied:

Data loading and inspection

Data splitting using stratified sampling

Feature scaling using StandardScaler

Model training using pipelines

Model evaluation and comparison

Model selection and saving

Deployment using FastAPI

🤖 Models Used

Two machine learning models were trained and compared:

Logistic Regression

XGBoost Classifier

The comparison was based on multiple evaluation metrics to select the best-performing model.

📈 Evaluation Metrics

The models were evaluated using:

Precision

Recall

F1-score

ROC-AUC

Confusion Matrix

ROC Curve

Precision-Recall Curve

Due to the imbalanced nature of the dataset, ROC-AUC and Precision-Recall curves were especially emphasized.

✅ XGBoost achieved the best overall performance and was selected for deployment.

🚀 Deployment

The final model was deployed as a web-based application using FastAPI.

Key Features:

RESTful API for predictions

Interactive web interface (GUI)

JSON-based transaction input

Real-time fraud prediction with probability score

🖥️ Web Interface

The web interface allows users to:

Enter transaction data in JSON format

Send data to the ML model

Receive predictions:

Legit ✅

Fraud ❌

View the predicted probability of fraud

▶️ How to Run the Project
1️⃣ Clone the repository
git clone <repository-url>
cd project-folder

2️⃣ Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
uvicorn main:app --reload

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
│   │
│   ├── templates/
│   │   └── index.html
│   │
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

The focus is on real-world applicability and model performance.

The system demonstrates a complete Machine Learning End-to-End workflow.

🏁 Conclusion

This project showcases how machine learning can be effectively used to address real-world financial fraud problems by combining data preprocessing, model evaluation, and deployment into a single integrated system.
