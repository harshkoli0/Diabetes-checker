# 🩺 Diabetes Prediction Web App

This is a machine learning web application built with **Flask** that predicts whether a person is diabetic or not based on several medical parameters. The backend model is trained using the **Pima Indians Diabetes Dataset** and uses a **Logistic Regression** classifier.

🔗 **Live Demo**: [https://diabetes-checker-koli8.onrender.com](https://diabetes-checker-koli8.onrender.com)

---

## 🚀 Features

- Simple and interactive user interface
- Takes 8 medical input parameters
- Predicts whether the user is Diabetic or Not Diabetic
- Built using Flask and deployed on Render

---

## 📊 Input Parameters

The model uses the following input features:

1. Pregnancies
2. Glucose
3. Blood Pressure
4. Skin Thickness
5. Insulin
6. BMI
7. Diabetes Pedigree Function
8. Age

---

## 🧠 Model Used

- Algorithm: **Logistic Regression**
- Library: `scikit-learn`
- Trained on: **Pima Indians Diabetes Dataset**

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML/CSS (for UI)
- Scikit-learn (ML model)
- Numpy & Pandas
- Render (Deployment)

---

## 📂 Project Structure

daibites_project/
│
├── app.py                 # ✅ Main Flask application
├── daibites.pkl           # ✅ Trained Machine Learning model (Logistic Regression, etc.)
  
                          
                          
│
├── templates/             # ✅ HTML templates
│   ├── index.html         #     Input form page
│   └── result.html        #     (Optional) Separate result page
│


├── static/                # ✅ Static files (CSS, JS, images if needed)
│
├── requirements.txt       # ✅ Project dependencies
└── README.md              # ✅ Project description, instructions, and deployment link
