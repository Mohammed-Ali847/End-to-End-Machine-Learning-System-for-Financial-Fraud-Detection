📌 نبذة عن المشروع (بالعربية)

يهدف هذا المشروع إلى بناء نظام متكامل للكشف عن عمليات الاحتيال المالي (Fraud Detection) باستخدام تقنيات تعلم الآلة، وذلك من خلال إعداد خط معالجة بيانات (Pipeline) احترافي، تدريب ومقارنة نماذج تعلم آلة متعددة، وتقييم أدائها باستخدام مقاييس مناسبة لطبيعة البيانات غير المتوازنة، ثم نشر النموذج الأفضل كخدمة API.

المشروع مطبّق بأسلوب End-to-End Machine Learning وفق متطلبات المقرر.

📌 Project Overview (English)

This project aims to build an end-to-end machine learning system for financial fraud detection.
The workflow includes data preprocessing, pipeline construction, training and comparing multiple models, evaluating their performance, and deploying the best-performing model as an API service.

The project follows academic best practices and fulfills all course requirements.

👥 Team Members

محمد جميل عبد القادر قايد

جبران صالح علي جبران

حلمي خميس جبران

📂 Dataset

Dataset: Credit Card Transactions Dataset

Description:
The dataset contains anonymized transaction features (V1–V28), transaction amount, time, and a binary target variable indicating fraud.

Challenge:
Highly imbalanced classes (fraud cases are rare).

🧠 Machine Learning Pipeline

The project is structured into clear and well-defined stages:

Exploratory Data Analysis (EDA)

Data inspection

Class distribution analysis

Basic statistics and visualization

Data Preprocessing

Train/Test split with stratification

Feature scaling using StandardScaler

Pipeline construction to avoid data leakage

Model Training

Logistic Regression (Baseline Model)

XGBoost Classifier (Advanced Model)

Model Evaluation

Confusion Matrix

Precision, Recall, F1-score

ROC-AUC Curve

Model comparison and selection

Deployment

Model export

API development using FastAPI / Flask

Optional Docker containerization

🧪 Models Used

Logistic Regression

XGBoost Classifier

XGBoost was selected due to its strong performance on structured and imbalanced datasets.

🛠️ Technologies & Libraries

Python

NumPy

Pandas

Scikit-learn

XGBoost

Matplotlib / Seaborn

FastAPI / Flask

Docker (Optional)

📁 Project Structure
ML-Fraud-Detection/
│
├── data/
│   └── creditcard.csv
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing_Pipeline.ipynb
│   ├── 03_Model_Training.ipynb
│   └── 04_Evaluation.ipynb
│
├── app/
│   ├── main.py
│   └── schemas.py
│
├── models/
│   └── best_model.pkl
│
├── requirements.txt
├── README.md
└── report.pdf

🚀 How to Run

Install dependencies:

pip install -r requirements.txt


Run notebooks in order:

01 → 02 → 03 → 04


Start the API:

uvicorn app.main:app --reload

📄 Final Report

A detailed academic report is included in report.pdf, explaining all steps, experiments, and results.

⭐ Notes

The project focuses on a real-world financial problem.

All experiments were conducted following academic and ethical guidelines.

The codebase is modular, clean, and well-documented.
