# 🌧️ Malaysia Flood Prediction System

## 📌 Project Overview
The Malaysia Flood Prediction System is a Machine Learning-powered web application designed to act as a decision support tool for assessing flood risks across various states and territories in Malaysia. By leveraging historical weather data and an optimized classifier, this tool provides real-time flood risk assessments based on user-defined meteorological parameters.

## 🚀 Live Demo
Experience the live deployed application here:
👉 [https://pdyrnigfeoinwughjvmubk.streamlit.app/](https://pdyrnigfeoinwughjvmubk.streamlit.app/)

## 🧠 Machine Learning Architecture

### 1. The Model
The core prediction engine is built upon an optimized Classification Model (`flood_prediction_model.pkl`). The backend is engineered to process clean environmental features to safeguard against synthetic variance and ensure highly reliable predictive outputs.

### 2. Feature Engineering & Robustness (Data Leakage Mitigation)
The latest version of the model utilizes **17 distinct features** (optimized down from 20). Crucially, historical target-leakage features such as `Year` and `Annual_Rainfall` have been strictly eliminated from the pipeline to prevent data leakage and ensure realistic production-grade evaluation.

To maximize user experience (UX) without compromising the model's integrity, the frontend takes **4 critical user inputs**, while the remaining baseline meteorological attributes are dynamically handled by the system pipeline:

* **User Inputs (Dynamic via UI):**
  * Target State / Territory (Automatically mapped to geographical numerical encodings)
  * Monthly Rainfall (mm) *(Seamlessly mapped to `Precipitation_Total`)*
  * Relative Humidity (%)
  * Average Temperature (°C)
* **System Imputed (Baseline Constants):** `Month`, `District_Code`, `Pressure`, `Dew_Point`, `Wind_Speed`, `Gust`, `Wind_Chill`, `UV_Index`, `Feel_Like_Temp`, `Visibility`, `Solar_Radiation`, `Pollutant_Value`, and `Precipitation_Rate`.

### 3. Caching Mechanism
The app utilizes Streamlit's `@st.cache_resource` decorator to load the heavy `.pkl` model file only once upon initialization. This drastically reduces the computational overhead and ensures instantaneous prediction updates whenever users adjust frontend sliders.

## 🛠️ Technology Stack
* **Frontend & Deployment:** Streamlit / Streamlit Community Cloud
* **Data Manipulation:** Pandas / NumPy
* **Machine Learning:** Scikit-Learn
* **Model Serialization:** Joblib

## 📂 Repository Structure
```text
├── .devcontainer/                 # Development container configuration
├── flood_app.py                   # Main Streamlit application script
├── flood_prediction_model.pkl     # Pre-trained optimized model (17 features)
├── requirements.txt               # Project production dependencies
└── README.md                      # Project documentation
