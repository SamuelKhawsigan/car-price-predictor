import pandas as pd
import joblib
import os

# path of the current file to help locate the .pkl file
# make sure it works even if you run the script from different folders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'malaysia_car_predictor.pkl')

def load_trained_model():
    """loads the Random Forest model."""
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

def get_prediction(age, mileage, brand='Other'):
    """
    Predicts car price based on age, mileage, and brand.
    Defaults to 'Other' if brand isn't in top 10.
    """
    model = load_trained_model()
    
    # Create an empty template with 0s for all columns
    feature_names = model.feature_names_in_
    input_df = pd.DataFrame(0, index=[0], columns=feature_names)
    
    # Set the car age and mileage
    input_df['Car_Age'] = age
    input_df['Milleage'] = mileage
    
    # Set the brand (e.g., 'Model_Filtered_Honda')
    brand_col = f'Model_Filtered_{brand}'
    if brand_col in input_df.columns:
        input_df[brand_col] = 1
    
    prediction = model.predict(input_df)[0]
    return round(prediction, 2)

if __name__ == "__main__":
    #test to make sure it works
    print("Testing Model Logic...")
    try:
        test_val = get_prediction(age=5, mileage=60000, brand='Honda')
        print(f"Test Success! 5yr Honda (60k KM) predicted at: RM {test_val:,}")
    except Exception as e:
        print(f"Test Failed: {e}")