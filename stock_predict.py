import pandas as pd
import numpy as np
from datetime import datetime
from alpha_vantage.timeseries import TimeSeries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Function to fetch stock data from Alpha Vantage API
def fetch_stock_data(symbol):
    api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, _ = ts.get_daily(symbol=symbol, outputsize='full')
    return data

# Function to calculate the percentage increase in stock price over a specified time horizon
def calculate_percentage_increase(data, years):
    closing_prices = data['4. close']
    initial_price = closing_prices.iloc[0]
    final_price = closing_prices.iloc[-1]
    percentage_increase = ((final_price - initial_price) / initial_price) * 100
    return percentage_increase / years

# Function to train a simple linear regression model to predict stock price movement
def train_linear_regression_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return model, mse

# Main function
def main():
    # Ask the user to input the file location of the Excel sheet containing historical stock data
    file_location = input("Please enter the file location of the Excel sheet containing historical stock data: ")
    
    # Load historical stock data from the Excel sheet
    df = pd.read_excel(file_location)
    
    # Fetch most recent stock data from Alpha Vantage API
    symbol = input("Please enter the stock symbol (e.g., AAPL): ")
    recent_data = fetch_stock_data(symbol)
    
    # Calculate percentage increase in stock price over the next 5 years and 10 years
    five_year_increase = calculate_percentage_increase(df, 5)
    ten_year_increase = calculate_percentage_increase(df, 10)
    print(f"The stock is expected to increase by {five_year_increase:.2f}% over the next 5 years.")
    print(f"The stock is expected to increase by {ten_year_increase:.2f}% over the next 10 years.")
    
    # Prepare data for training the machine learning model
    X = df[['Open', 'High', 'Low', 'Volume']].values
    y = df['Close'].values
    
    # Train a linear regression model
    model, mse = train_linear_regression_model(X, y)
    print(f"Mean Squared Error of the model: {mse}")
    
    # Predict if the stock price will increase in the next 10 years
    last_data_point = X[-1].reshape(1, -1)
    prediction_next_10_years = model.predict(last_data_point)
    if prediction_next_10_years > df['Close'].iloc[-1]:
        print("The model predicts that the stock price will increase in the next 10 years.")
    else:
        print("The model predicts that the stock price will decrease or remain the same in the next 10 years.")

if __name__ == "__main__":
    main()
