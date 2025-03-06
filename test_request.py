import requests

url = "http://127.0.0.1:8000/predict/"  # ✅ Ensure this URL is correct
data = {
    "Age": 16,
    "Gender": 0,
    "Ethnicity": 1,
    "ParentalEducation": 2,
    "StudyTimeWeekly": 8,
    "Absences": 3,
    "Tutoring": 0,
    "ParentalSupport": 1,
    "Extracurricular": 1,
    "Sports": 1,
    "Music": 0,
    "Volunteering": 1
}

response = requests.post(url, json=data)  # ✅ Ensure this is `post`, NOT `get`
print(response.json())
