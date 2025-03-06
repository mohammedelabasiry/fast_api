

import pickle
# from pycaret.classification import load_model, predict_model
import pandas as pd
from fastapi import FastAPI, Query

# إنشاء التطبيق
app = FastAPI()
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)
# تحميل النموذج المدرب
# model = load_model("student_performance_model.pkl")
# model_path = os.path.abspath("student_performance_model.pkl")

# Load model
# model = load_model(model_path)
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Student Performance Prediction API"}
@app.get("/predict")
async def predict(
    Age: int = Query(..., description="عمر الطالب (من 15 إلى 18 سنة)"),
    Gender: int = Query(..., description="جنس الطالب (0: ذكر، 1: أنثى)"),
    Ethnicity: int = Query(..., description="العرق (0: قوقازي، 1: أفريقي أمريكي، 2: آسيوي، 3: آخر)"),
    ParentalEducation: int = Query(..., description="مستوى تعليم الأهل (0: بدون شهادة، 1: مدرسة ثانوية، 2: دبلوم، 3: بكالوريوس، 4: أعلى)"),
    StudyTimeWeekly: float = Query(..., description="وقت الدراسة الأسبوعي (بالساعات، من 0 إلى 20)"),
    Absences: int = Query(..., description="عدد مرات الغياب خلال العام الدراسي (من 0 إلى 30)"),
    Tutoring: int = Query(..., description="الحصول على دروس خصوصية (0: لا، 1: نعم)"),
    ParentalSupport: int = Query(..., description="يوجد دعم من الأهل (0: لا، 1: متوسط، 2: عالي)"),
    Extracurricular: int = Query(..., description="المشاركة في أنشطة لا منهجية (0: لا، 1: نعم)"),
    Sports: int = Query(..., description="المشاركة في الأنشطة الرياضية (0: لا، 1: نعم)"),
    Music: int = Query(..., description="المشاركة في الأنشطة الموسيقية (0: لا، 1: نعم)"),
    Volunteering: int = Query(..., description="المشاركة في العمل التطوعي (0: لا، 1: نعم)"),
    ):
   
    data = {
    "Age": Age,
    "Gender": Gender,
    "Ethnicity": Ethnicity,
    "ParentalEducation": ParentalEducation,
    "StudyTimeWeekly": StudyTimeWeekly,
    "Absences": Absences,
    "Tutoring": Tutoring,
    "ParentalSupport": ParentalSupport,
    "Extracurricular": Extracurricular,
    "Sports": Sports,
    "Music": Music,
    "Volunteering": Volunteering
    }
    df = pd.DataFrame([data])

    # إجراء التنبؤ
    predictions = model.predict(df)

    # استخراج التنبؤ
    predicted_grade = predictions["prediction_label"].iloc[0]

    grade_map = {
        0: "ممتاز (90-100%)",
        1: "جيد جداً (80-89%)",
        2: "جيد (70-79%)",
        3: "مقبول (60-69%)",
        4: "راسب (أقل من 60%)"
    }

    grade = grade_map.get(predicted_grade, "غير معروف")

    return {"الدرجة المتوقعة": grade}

   