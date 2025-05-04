from joblib import load

# Paths to your saved model and scaler files (adjust as needed)
MODEL_PATH = "crop_recomendation_model4.pkl"
STANDARED_SCALER_PATH = "standardsclar4.pkl"

# Load model and scaler once during initialization
model = load(MODEL_PATH)
standard_scaler = load(STANDARED_SCALER_PATH)

def recommend_crop(features):
    """
    Recommends a crop based on input features using a pre-trained ML model.

    Args:
        features (list): A list of input features [N, P, K, temperature, humidity, pH, rainfall].

    Returns:
        str: The recommended crop name or an error message.
    """
    try:
        # Scale the input features
        scaled_features = standard_scaler.transform([features])
        
        # Predict the crop index
        predicted_index = model.predict(scaled_features)[0]
        
        # Map index to crop name
        crop_names = {
          0: 'apple', 1: 'banana', 2: 'blackgram', 3: 'chickpea', 4: 'coconut', 5: 'coffee',
        6: 'cotton', 7: 'grapes', 8: 'jute', 9: 'kidneybeans', 10: 'lentil', 11: 'maize',
        12: 'mango', 13: 'mothbeans', 14: 'mungbean', 15: 'muskmelon', 16: 'orange',
        17: 'papaya', 18: 'pigeonpeas', 19: 'pomegranate', 20: 'rice', 21: 'watermelon'
        }
        
        return crop_names.get(predicted_index, "Unknown Crop")
    except Exception as e:
        return f"Error in recommendation: {str(e)}"


