# End-to-End-Machine-Learning-System-for-Financial-Fraud-Detection
# 💳 Financial Fraud Detection using Machine Learning

## 📌 نبذة عن المشروع (بالعربية)
يهدف هذا المشروع إلى بناء **نظام تعلم آلة متكامل (End-to-End)** للكشف عن عمليات الاحتيال المالي في المعاملات البنكية.  
يشمل المشروع جميع مراحل تعلم الآلة بدءًا من استكشاف البيانات ومعالجتها، مرورًا بتدريب ومقارنة عدة نماذج تعلم آلة (بما في ذلك نماذج متقدمة)، وتقييم أدائها باستخدام مقاييس مناسبة لطبيعة المشكلة، وانتهاءً بنشر النموذج الأفضل كخدمة API مع واجهة استخدام بسيطة.

تم تنفيذ هذا المشروع كجزء من متطلبات **مادة تعلم الآلة**، وبإشراف وموافقة الدكتور على استخدام خوارزميات متقدمة لتحسين الأداء.

---

## 📌 Project Overview (English)
This project presents an **End-to-End Machine Learning system** for detecting fraudulent financial transactions.  
It covers the complete ML lifecycle, including data exploration, preprocessing, training and comparing multiple machine learning models (including advanced models), performance evaluation using appropriate metrics, and deployment of the best-performing model as an API with a user-friendly interface.

The project is developed as part of the **Machine Learning course**, with instructor approval for using advanced models to enhance performance.

---

## 🎯 Objectives
- Use a **large, real-world financial dataset**
- Build a complete **Machine Learning Pipeline**
- Train and compare **multiple ML models (baseline and advanced)**
- Handle **highly imbalanced data**
- Evaluate models using **appropriate performance metrics**
- Deploy the best-performing model using **FastAPI**
- Provide a clean and user-friendly output interface

---

## 📊 Dataset
- **Name:** Credit Card Fraud Detection Dataset  
- **Description:** Contains anonymized credit card transactions labeled as fraudulent or legitimate  
- **Size:** Approximately 280,000 transactions  
- **Main Challenge:** Highly imbalanced data  

---

## 🧠 Machine Learning Models
The following models are implemented and compared:
- **Logistic Regression** (Baseline model)
- **Random Forest Classifier**
- **XGBoost Classifier** (Advanced model for performance optimization)

---

## 📈 Evaluation Metrics
Due to the imbalanced nature of the dataset, the following metrics are used:
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix
- Precision-Recall Curve

---

## 🌐 Deployment
- The best-performing trained model is deployed as a **REST API** using **FastAPI**
- A simple web interface allows users to input transaction data and receive fraud predictions along with risk probability

---

## 🛠️ Technologies Used
- Python
- NumPy, Pandas
- Scikit-learn
- XGBoost
- Matplotlib / Seaborn
- FastAPI
- HTML / CSS
- Git & GitHub

---

## 📂 Project Structure
fraud-detection-ml/
│
├── data/ # Dataset files
├── notebooks/ # Jupyter notebooks (EDA, experiments)
├── src/ # ML pipeline and model code
├── api/ # FastAPI application
├── reports/ # Project report (PDF)
├── requirements.txt # Project dependencies
└── README.md

---

## 👥 Team Members
- **محمد جميل عبد القادر قايد**
- **جبران صالح علي جبران**
- **حلمي خميس جبران**

---

## 📄 License
This project is developed for educational purposes as part of a university course.
