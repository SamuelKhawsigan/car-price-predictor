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


## 📊 Data Source & Credits

The dataset used in this project consists of approximately 1,000 used car listings from the Malaysian market, specifically focusing on the Kuala Lumpur and Selangor regions.

* **Primary Source:** The data was sourced from a publicly available [Malaysia Car Dataset](https://www.kaggle.com/datasets/tanshihjen/malaysia-resale-carlist) on Kaggle
* **Data Context:** The raw data included information on 168 unique car models, including popular local brands like Proton, as well as international brands like Toyota, Honda, and BMW.
* **Processing:** I would like to credit the original data contributors for providing a comprehensive look into local vehicle depreciation, which made the training of this Random Forest model possible.