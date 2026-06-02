import streamlit as st
import pandas as pd
import joblib

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Malaysia Flood Prediction",
    page_icon="🌧️",
    layout="wide"
)

# ==========================================
# 2. LOAD PRE-TRAINED MODEL
# ==========================================
@st.cache_resource
def load_model():
    return joblib.load('flood_prediction_model.pkl')

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading the model. Please ensure 'flood_prediction_model.pkl' is uploaded in your directory. Details: {e}")
    st.stop()

# ==========================================
# 3. STATE ENCODING MAPPING
# ==========================================
state_mapping = {
    "Johor": 1,
    "Kedah": 2,
    "Kelantan": 3,
    "Melaka": 4,
    "Negeri Sembilan": 5,
    "Pahang": 6,
    "Penang": 7,
    "Perak": 8,
    "Perlis": 9,
    "Sabah": 10,
    "Sarawak": 11,
    "Selangor": 12,
    "Terengganu": 13,
    "Kuala Lumpur": 14,
    "Labuan": 15,
    "Putrajaya": 16
}

# ==========================================
# 4. USER INTERFACE (GUI)
# ==========================================
st.title("🌧️ Malaysia Flood Prediction")
st.markdown("Decision support tool for assessing flood risk across Malaysian states and territories")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1 — WEATHER PARAMETERS")

    selected_state = st.selectbox("Target State / Territory", list(state_mapping.keys()))
    rainfall = st.slider("Monthly Rainfall (mm)", 0, 1000, 250)
    humidity = st.slider("Relative Humidity (%)", 0, 100, 85)
    temperature = st.number_input("Average Temperature (°C)", value=27.50, step=0.10)

    analyze_btn = st.button("▶ Run Flood Risk Analysis")

with col2:
    st.subheader("2 — PREDICTION OUTPUT")

    if analyze_btn:
        state_code = state_mapping[selected_state]

        # ==========================================
        # 5. DATA PREPARATION (17 Features)
        # ==========================================
        input_data = pd.DataFrame({
            "Month": [5],
            "State_Code": [state_code],
            "District_Code": [1],
            "Temperature": [temperature],
            "Pressure": [1010.5],
            "Dew_Point": [24.0],
            "Humidity": [humidity],
            "Wind_Speed": [10.0],
            "Gust": [15.0],
            "Wind_Chill": [temperature],
            "UV_Index": [6.0],
            "Feel_Like_Temp": [temperature + 1.5],
            "Visibility": [10.0],
            "Solar_Radiation": [200.0],
            "Pollutant_Value": [50.0],
            "Precipitation_Rate": [0.0],
            "Precipitation_Total": [rainfall]
        })

        # ==========================================
        # 6. MODEL PREDICTION
        # ==========================================
        try:
            prediction = model.predict(input_data)

            if prediction[0] == 1:
                st.error("🚨 **High Flood Risk Detected!**")
                st.markdown("Please take necessary precautions and alert local authorities.")
            else:
                st.success("✅ **Low Flood Risk.**")
                st.markdown("Weather conditions are currently within safe parameters.")

        except Exception as e:
            st.warning(f"Prediction Error. Please ensure the model features match. Details: {e}")

    else:
        st.info("☁️ Set parameters on the left and click **Run Flood Risk Analysis**")
