# 🏙️ Bengaluru Flat Price Prediction Web App

A Machine Learning web application built with **Flask**, **Scikit-Learn**, and **Tailwind CSS** that predicts house and flat prices in Bengaluru across **250+ locations** based on location, square footage, BHK, and bathroom count.

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.x-black.svg)
![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-1.6.1-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📌 Features

- 🎯 **250+ Locality Coverage**: Covers major real estate hubs in Bangalore (Indiranagar, Whitefield, Jayanagar, Electronic City, Koramangala, etc.).
- ⚡ **Instant ML Valuation**: Uses a pre-trained **Ridge Regression** model pipeline to estimate property value in **Lakhs (₹)** with automatic **Crore (Cr)** conversion.
- 🔍 **Live Search Location Dropdown**: Filter through 250+ locations dynamically as you type.
- ⚡ **Preset Sample Buttons**: One-click selection for popular Bengaluru neighborhoods to quickly test predictions.
- 🎨 **Monochrome Dark Mode UI**: Built with Tailwind CSS featuring a glassmorphism aesthetic.
- 🛡️ **Input Validation & Error Handling**: Real-time client-side & server-side validation for clean user input.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.12, Flask 3.x
- **Machine Learning**: Scikit-Learn (Ridge Regression), Pandas, NumPy, Pickle
- **Frontend**: HTML5, JavaScript (Fetch API), Tailwind CSS (CDN)
- **Dataset**: Bengaluru House Price Cleaned Dataset

---

## 📁 Repository Structure

```text
├── app.py               # Main Flask backend application & API routes
├── Cleaned_data.csv     # Cleaned dataset containing valid Bengaluru locations
├── RidgeModel.pkl       # Serialized Scikit-learn Ridge Regression model
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Web UI template (Tailwind CSS + JS)
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Tanmaychandekar45/Banglore-flat-price-prediction-model.git
cd Banglore-flat-price-prediction-model
```

### 2. Install Dependencies

It is recommended to use **Python 3.12**.

```bash
pip install -r requirements.txt
```

*Or on Windows using Python Launcher:*
```bash
py -3.12 -m pip install -r requirements.txt
```

### 3. Run the Flask Server

```bash
python app.py
```

*Or with Python Launcher:*
```bash
py -3.12 app.py
```

### 4. Access the Web App

Open your browser and navigate to:
```text
http://127.0.0.1:5000
```

---

## 🔌 API Endpoint

### `POST /predict`

Predict property price given property specification parameters.

#### Request Header:
`Content-Type: application/json`

#### Request Body Example:
```json
{
  "location": "Whitefield",
  "total_sqft": 1250,
  "bhk": 2,
  "bath": 2
}
```

#### Response Example:
```json
{
  "success": true,
  "prediction": "51.84",
  "price_lakhs": 51.84,
  "unit": "Lakhs"
}
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Tanmaychandekar45/Banglore-flat-price-prediction-model/issues).

---

## 📄 License

This project is licensed under the MIT License.
