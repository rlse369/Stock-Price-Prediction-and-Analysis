import stock_analysis_project.data_collection
import stock_analysis_project.data_preprocessing
import stock_analysis_project.eda
import stock_analysis_project.time_series_analysis
import stock_analysis_project.feature_engineering
import stock_analysis_project.modeling

def main():
    print("\n📥 Step 1: Fetching Data...")
    stock_analysis_project.data_collection.fetch_stock_data()
    
    print("\n🔄 Step 2: Preprocessing Data...")
    stock_analysis_project.data_preprocessing.preprocess_data()
    
    print("\n📊 Step 3: Running EDA...")
    stock_analysis_project.eda.run_eda()
    
    print("\n📈 Step 4: Running Time Series Analysis...")
    stock_analysis_project.time_series_analysis.run_time_series_analysis()

    print("\n🛠 Step 5: Creating Features...")
    stock_analysis_project.feature_engineering.create_features()

    print("\n🤖 Step 6: Training LSTM Model...")
    stock_analysis_project.modeling.train_model()

    print("\n✅ Stock Analysis Completed!")

if __name__ == "__main__":
    main()
