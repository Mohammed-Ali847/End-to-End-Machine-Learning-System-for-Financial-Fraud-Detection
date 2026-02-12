🧠 Credit Card Fraud Detection System

Machine Learning End-to-End Project



📌 Project Overview

This project aims to analyze youth unemployment rates across different countries and years, and to explore their distribution and relationship with GDP per capita.
The project focuses on data analysis and anomaly detection, following a structured data science workflow.

📂 Datasets Used

Two real-world datasets were used:

Youth Unemployment Dataset

Contains youth unemployment rates (%) for different countries over multiple years.

Key columns:

Country

CountryCode

Year

YouthUnemployment

GDP per Capita Dataset

Contains GDP per capita values (US$) for countries across multiple years.

Originally provided in wide format and later transformed to long format.

🔧 Data Preprocessing

The following preprocessing steps were applied:

Removal of missing values in critical columns (YouthUnemployment, GDP_per_Capita, Country, Year)

Transformation of the GDP dataset from wide to long format using melt

Standardization of column names

Merging datasets using Country and Year

Checking for duplicate rows

This approach ensures clean and reliable data for analysis.

📊 Exploratory Data Analysis (EDA)

EDA was performed to understand the structure and behavior of the data:

Histogram to analyze the distribution of youth unemployment rates

Boxplot to detect outliers and data spread

Scatter plot to explore the relationship between GDP per capita and youth unemployment

Correlation analysis between key variables

🚨 Outlier Detection Algorithms

Two anomaly detection algorithms were used to identify unusual patterns in youth unemployment data:

1️⃣ Isolation Forest

An unsupervised learning algorithm designed for anomaly detection.

Works by randomly partitioning the data.

Data points that are isolated quickly are considered outliers.

Suitable for large and high-dimensional datasets.

2️⃣ Local Outlier Factor (LOF)

Detects anomalies based on local data density.

Compares each data point to its neighbors.

Points with significantly lower density than their neighbors are labeled as outliers.

Effective in identifying local anomalies.

Both algorithms were used to support the identification of abnormal youth unemployment rates.

📈 Key Findings

Most countries show moderate youth unemployment rates.

A small number of observations exhibit extremely high youth unemployment, identified as outliers.

GDP per capita alone does not strongly explain youth unemployment levels.

Structural and social factors likely play a major role.

🧠 Conclusion

This project demonstrates the importance of exploratory data analysis and anomaly detection in economic data.
Using Isolation Forest and Local Outlier Factor helped identify unusual unemployment patterns that are not easily observable through simple statistics.

The results highlight that youth unemployment is a complex issue influenced by multiple factors beyond economic output.

🛠 Tools & Libraries

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Jupyter Notebook

📄 Output

Jupyter Notebook containing:

Data cleaning

EDA

Outlier detection

Visualizations

Final report (PDF)

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
