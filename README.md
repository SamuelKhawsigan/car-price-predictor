# 🚗 Malaysia Car Price Predictor
A machine learning tool built to estimate used car prices in the Malaysian market.

### 🛠️ Technical Implementation
* **Model:** Random Forest Regressor (chosen over Linear Regression for better handling of non-linear depreciation).
* **Data Sanitization:** Aggressive cleaning of 'RM', commas, and mileage ranges from raw scrapings.
* **Market Segmentation:** Focused on cars < RM 200,000 to reduce outlier noise and improve real-world accuracy.

### 🚀 Usage
```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python -m src.model