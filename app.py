import pickle
import os
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Base directory for relative paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "Cleaned_data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "RidgeModel.pkl")

# Load dataset and extract unique locations
try:
    df = pd.read_csv(DATA_PATH)
    locations = sorted(df["location"].dropna().unique().tolist())
except Exception as e:
    locations = []
    print(f"Error loading Cleaned_data.csv: {e}")

# Load pre-trained Ridge Regression model
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    model = None
    print(f"Error loading RidgeModel.pkl: {e}")


@app.route("/")
def index():
    return render_template("index.html", locations=locations)


@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"success": False, "error": "Model file not loaded on server."}), 500

    try:
        data = request.get_json(silent=True) or request.form
        location = data.get("location")
        total_sqft = data.get("total_sqft")
        bath = data.get("bath")
        bhk = data.get("bhk")

        if not location:
            return jsonify({"success": False, "error": "Please select a location."}), 400

        try:
            total_sqft = float(total_sqft)
            bath = float(bath)
            bhk = int(bhk)
        except (ValueError, TypeError):
            return jsonify({"success": False, "error": "Square footage, Bathrooms, and BHK must be valid numbers."}), 400

        if total_sqft <= 0:
            return jsonify({"success": False, "error": "Total square feet must be greater than 0."}), 400

        if bath <= 0 or bhk <= 0:
            return jsonify({"success": False, "error": "Bathrooms and Bedrooms (BHK) must be greater than 0."}), 400

        # Construct DataFrame matching the model training features
        input_df = pd.DataFrame(
            [[location, total_sqft, bath, bhk]],
            columns=["location", "total_sqft", "bath", "bhk"]
        )

        prediction = model.predict(input_df)[0]
        # Prevent negative predictions if model output drops below 0 for extreme out-of-bounds inputs
        price_lakhs = max(0.0, float(prediction))
        formatted_price = f"{price_lakhs:.2f}"

        return jsonify({
            "success": True,
            "prediction": formatted_price,
            "price_lakhs": price_lakhs,
            "unit": "Lakhs"
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
