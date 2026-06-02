# 🌧️ Malaysia Flood Prediction System

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📌 Project Overview
The **Malaysia Flood Prediction System** is a Machine Learning-powered web application designed to act as a decision support tool for assessing flood risks across various states and territories in Malaysia. By leveraging historical weather data and an optimized Random Forest classifier, this tool provides real-time flood risk assessments based on user-defined meteorological parameters.

## 🚀 Live Demo
[https://flqchayik2aomgkfkwzpvb.streamlit.app/](https://5mu4biflxlsfdlxrhoi66a.streamlit.app/)

---

## 🧠 Machine Learning Architecture

### 1. The Model
The core prediction engine is built upon a **Random Forest Classifier** (`flood_prediction_model.pkl`). Random Forest was selected for its robustness against overfitting and its high accuracy in handling non-linear environmental datasets. 

### 2. Feature Engineering & Data Preparation
The model was trained on a comprehensive dataset requiring **20 distinct features**. To maximize user experience (UX) without compromising the model's integrity, the frontend is designed to take **4 critical user inputs**, while the remaining features are dynamically imputed using strategic baseline values:

* **User Inputs (Dynamic):**
    * Target State / Territory (Mapped to numerical encodings)
    * Monthly Rainfall (mm)
    * Relative Humidity (%)
    * Average Temperature (°C)
* **System Imputed (Baseline):** Year, Month, Pressure, Dew Point, Wind Speed, Gust, Wind Chill, UV Index, Feel Like Temp, Visibility, Solar Radiation, Pollutant Value, Precipitation rates, and Annual Rainfall.

### 3. Caching Mechanism
The app utilizes Streamlit's `@st.cache_resource` decorator to load the heavy `.pkl` file only once upon initialization. This drastically reduces the computational overhead and ensures instantaneous predictions when users adjust the parameters.

---

## 🛠️ Technology Stack
* **Frontend & Deployment:** Streamlit / Streamlit Community Cloud
* **Data Manipulation:** Pandas
* **Machine Learning:** Scikit-Learn (Random Forest)
* **Model Serialization:** Joblib

---

## 📂 Repository Structure

```text
├── flood_app.py                   # Main Streamlit application script
├── flood_prediction_model.pkl     # Pre-trained Random Forest model
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation
