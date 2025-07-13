# ❤️ Heart Disease Predictor 

A machine learning–powered Flask web application that predicts whether a person is at risk of heart disease based on medical parameters.
This project uses a trained ML model and provides an interactive web interface for users to input their details and get predictions instantly.

## 🚀 Live Demo:-

🌐 View App on Render -  https://heart-disease-predictor-6wsi.onrender.com 


## 📋 Features:-

✅ Predicts risk of heart disease using trained model
✅ Interactive web form with validation
✅ Clean and responsive UI (Bootstrap)
✅ Deployed on Render, ready to use

## 🗂️ Project Structure:-

heart_disease_project/
├── app.py                # Flask application
├── model/
│   └── heart_model.pkl   # Trained machine learning model
├── templates/
│   ├── index.html        # Home page (form)
│   └── result.html       # Results page
├── static/
│   └── background.jpg    # Background image
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation


## 🛠️ Tech Stack:-

* Python 🐍
* Flask 🌟
* Scikit-learn 🤖
* Bootstrap 🎨
* Render (for deployment) ☁️


## 🧪 Sample Input:-

Feature	                  Example
-----------------------------------
Age	                       45
Sex	                       1
Chest Pain Type	           2
Resting BP	               120
Cholesterol	               240
Fasting Blood Sugar	       0
Resting ECG	               1
Max Heart Rate	           150
Exercise-induced Angina	   0
Oldpeak	                   1.4
Slope                      2
CA	                       0
Thal                       2

## 💻 Local Installation:-

### 🔷 Prerequisites;

* Python ≥ 3.7
* `pip`

### 🔷 Steps;

# clone the repo
git clone https://github.com/your-username/heart-disease-predictor.git
cd heart-disease-predictor

# create virtual environment
python -m venv .venv
# activate it
.venv\Scripts\activate    # on Windows
source .venv/bin/activate # on Linux/Mac

# install dependencies
pip install -r requirements.txt

# run the app
python app.py

## 🌐 Deployment (on Render);

1️⃣ Push your code to a GitHub repository.
2️⃣ Log in to [Render](https://render.com/) and create a new **Web Service**.
3️⃣ Connect your GitHub repo → set environment:

* Build Command: `pip install -r requirements.txt`
* Start Command: `gunicorn app:app`
  4️⃣ Deploy!

## 👤 Author:-

✨NIHARIKA SAXENA 
