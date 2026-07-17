import streamlit as st
from app import SmartFarmingAssistant

st.set_page_config(page_title="Smart Farming AI", page_icon="🌾", layout="wide")

st.title("Smart Farming AI Assistant")
st.write("Enter soil and weather values to get crop recommendations and farming advice.")

assistant = SmartFarmingAssistant()

with st.form("crop_form"):
    nitrogen = st.number_input("Nitrogen (N)", min_value=0.0, value=80.0)
    phosphorus = st.number_input("Phosphorus (P)", min_value=0.0, value=40.0)
    potassium = st.number_input("Potassium (K)", min_value=0.0, value=40.0)
    temperature = st.number_input("Temperature", min_value=-50.0, value=25.0)
    humidity = st.number_input("Humidity", min_value=0.0, max_value=100.0, value=60.0)
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=6.5)
    rainfall = st.number_input("Rainfall", min_value=0.0, value=120.0)
    submitted = st.form_submit_button("Predict Crop")

if submitted:
    raw_inputs = {
        "Nitrogen": nitrogen,
        "Phosphorus": phosphorus,
        "Potassium": potassium,
        "Temperature": temperature,
        "Humidity": humidity,
        "pH": ph,
        "Rainfall": rainfall,
    }
    try:
        processed_features = assistant.preprocessor.prepare_features(raw_inputs)
        predicted_crop, confidence = assistant.predictor.predict(processed_features)
        explanation = assistant.recommender.explain_crop_suitability(predicted_crop, raw_inputs)
        recommendations = assistant.recommender.generate_recommendations(predicted_crop, raw_inputs)

        st.success(f"Predicted Crop: {predicted_crop}")
        if confidence is not None:
            st.info(f"Confidence: {confidence * 100:.2f}%")
        st.write(f"Why this crop fits: {explanation}")
        st.subheader("Recommendations")
        for key, message in recommendations.items():
            st.write(f"- **{key.replace('_', ' ').title()}:** {message}")
    except Exception as exc:
        st.error(f"Prediction failed: {exc}")
