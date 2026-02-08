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

# 3. إنشاء تطبيق API
app = FastAPI(
    title="Financial Fraud Detection API",
    description="API to predict whether a credit card transaction is fraudulent.",
    version="1.0.0"
)

# إعداد الملفات الثابتة والقوالب
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# 4. تحميل النموذج المدرب
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

# 5. Endpoint لعرض الصفحة الرئيسية
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 7. Endpoint التنبؤ /predict
@app.post("/predict", response_model=PredictionResponse)
def predict(data: TransactionInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded on server. Please ensure best_model.pkl exists in models directory.")
    
    try:
        # تحويل البيانات إلى DataFrame بنفس ترتيب الخصائص أثناء التدريب
        input_dict = data.dict()
        input_df = pd.DataFrame([input_dict])
        
        # الحصول على التنبؤ
        prediction = int(model.predict(input_df)[0])
        
        # الحصول على الاحتمالية
        probability = float(model.predict_proba(input_df)[0][1])
        
        # تحديد التسمية النصية
        label = "Fraud" if prediction == 1 else "Normal"
        
        # 8. إرجاع النتيجة
        return {
            "prediction": prediction,
            "label": label,
            "probability": round(probability, 4)
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
