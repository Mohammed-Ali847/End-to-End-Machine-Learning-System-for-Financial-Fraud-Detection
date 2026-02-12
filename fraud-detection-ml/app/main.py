from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib
import pandas as pd
import numpy as np
import os

try:
    from .schemas import TransactionInput, PredictionResponse
except ImportError:
    from schemas import TransactionInput, PredictionResponse

# 1. إنشاء تطبيق API
app = FastAPI(
    title="Financial Fraud Detection API (Unsupervised)",
    description="API to detect fraudulent transactions using Unsupervised Anomaly Detection.",
    version="2.0.0"
)

# إعداد الملفات الثابتة والقوالب
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# التأكد من وجود المجلدات لتجنب الأخطاء
os.makedirs(os.path.join(BASE_DIR, "static"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "templates"), exist_ok=True)

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# 2. تحميل النموذج المدرب
MODEL_PATH = os.path.join(BASE_DIR, "models/best_model.pkl")
# إذا لم يكن في المجلد المحلي، نبحث في المجلد الأب (حسب هيكل المشروع)
if not os.path.exists(MODEL_PATH):
    MODEL_PATH = os.path.join(BASE_DIR, "../models/best_model.pkl")

model = None

@app.on_event("startup")
def load_model():
    global model
    try:
        if os.path.exists(MODEL_PATH):
            model = joblib.load(MODEL_PATH)
            print(f"Model loaded successfully from {MODEL_PATH}")
        else:
            print(f"Model file not found at {MODEL_PATH}")
    except Exception as e:
        print(f"Error loading model: {e}")

# 3. Endpoint لعرض الصفحة الرئيسية
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 4. Endpoint التنبؤ /predict
@app.post("/predict", response_model=PredictionResponse)
def predict(data: TransactionInput):
    if model is None:
        raise HTTPException(status_code=500,
                            detail="Model not loaded on server. Please ensure best_model.pkl exists in models directory.")

    try:
        # تحويل البيانات إلى DataFrame
        input_dict = data.dict()
        input_df = pd.DataFrame([input_dict])

        # الحصول على التنبؤ من Isolation Forest
        # يعيد 1 للبيانات الطبيعية و -1 للشواذ (الاحتيال)
        raw_prediction = model.predict(input_df)[0]
        
        # تحويل النتيجة إلى 0 (سليم) و 1 (احتيال)
        prediction = 1 if raw_prediction == -1 else 0
        
        # في التعلم غير الأشرافي (Isolation Forest)، نستخدم decision_function للحصول على درجة الشذوذ
        # القيم الأقل تعني شذوذ أكثر. سنقوم بتحويلها لنسبة تقريبية للعرض فقط.
        anomaly_score = model.decision_function(input_df)[0]
        # تحويل الدرجة إلى "احتمالية" تقريبية (كلما زاد الشذوذ زادت النسبة)
        # ملاحظة: هذه ليست احتمالية إحصائية دقيقة بل مؤشر لقوة الشذوذ
        probability = 1 / (1 + np.exp(anomaly_score * 10)) 

        label = "Fraud" if prediction == 1 else "Normal"

        return {
            "prediction": prediction,
            "label": label,
            "probability": round(float(probability), 4)
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
