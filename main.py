from src.model import get_prediction
import sys

def run_predictor():
    print("========================================")
    print(" MALAYSIA USED CAR PRICE PREDICTOR ")
    print("========================================\n")
    
    try:
        # 1. Capture User Input
        age = float(input("Enter the car's age (e.g., 5 for 2021 model): "))
        mileage = float(input("Enter the total mileage (KM): "))
        
        print("\nChoose a Brand (or press Enter for 'Other'):")
        print("Top Models: Mazda, Toyota, Honda, BMW, Ford, Proton, Kia")
        brand = input("Brand: ").strip().capitalize()
        
        if not brand:
            brand = 'Other'

        # 2. Get the Value from our Model
        estimated_price = get_prediction(age, mileage, brand)

        # 3. Display Result
        print("\n" + "-"*40)
        print(f"ESTIMATED MARKET VALUE: RM {estimated_price:,.2f}")
        print("-"*40)
        print("Disclaimer: This is an ML estimate for cars < RM 200k.")
        
    except ValueError:
        print("\n❌ Error: Please enter numbers for Age and Mileage.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_predictor()