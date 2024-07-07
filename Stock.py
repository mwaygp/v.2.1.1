import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Load data from Excel file
df = pd.read_excel('stock_data.xlsx')

# Drop unnecessary columns (e.g., date) and any rows with missing values
df.dropna(inplace=True)

# Feature engineering - Assuming 'Close' prices are our features
X = df[['Close']].values

# Target variable - Predict whether the stock price will increase (1) or decrease (0) in the next 10 years
# For simplicity, we'll assume if the stock price is higher after 10 years, it's considered an increase.
# You may adjust this logic based on your requirements.
y = np.where(df['Close'].shift(-120) > df['Close'], 1, 0)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Make predictions
predictions = model.predict(X_test_scaled)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Predict if the stock will increase in the next 10 years
# Let's take the last data point in the dataset for prediction
last_data_point = X[-1].reshape(1, -1)
last_data_point_scaled = scaler.transform(last_data_point)
prediction_next_10_years = model.predict(last_data_point_scaled)
if prediction_next_10_years[0] > 0.5:
    print("The model predicts that the stock price will increase in the next 10 years.")
else:
    print("The model predicts that the stock price will decrease or remain the same in the next 10 years.")
