import data_collection
import data_preprocessing
import eda
import time_series_analysis
import feature_engineering
import modeling

def main():
    print("\n📥 Step 1: Fetching Data...")
    data_collection.fetch_stock_data()
    
    print("\n🔄 Step 2: Preprocessing Data...")
    data_preprocessing.preprocess_data()
    
    print("\n📊 Step 3: Running EDA...")
    eda.run_eda()
    
    print("\n📈 Step 4: Running Time Series Analysis...")
    time_series_analysis.run_time_series_analysis()

    print("\n🛠 Step 5: Creating Features...")
    feature_engineering.create_features()

    print("\n🤖 Step 6: Training LSTM Model...")
    modeling.train_model()

    print("\n✅ Stock Analysis Completed!")

if __name__ == "__main__":
    main()
