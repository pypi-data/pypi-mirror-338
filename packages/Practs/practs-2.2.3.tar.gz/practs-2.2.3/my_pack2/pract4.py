#Implementing a context-aware recommender system

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import warnings

def main():
    warnings.filterwarnings('ignore')
    data = pd.DataFrame({
        'user_id': [1, 1, 2, 2, 3, 3],
        'item_id': [101, 102, 101, 103, 102, 104],
        'rating': [5, 4, 4, 5, 3, 2],
        'time_of_day': ['morning', 'evening', 'evening', 'morning', 'afternoon', 'evening'],
        'weather': ['sunny', 'rainy', 'rainy', 'sunny', 'cloudy', 'rainy']})
    context_features = pd.get_dummies(data[['time_of_day', 'weather']])
    data = pd.concat([data[['user_id', 'item_id', 'rating']], context_features], axis=1)
    data['user_id'] = data['user_id'].astype(str) + "_" + data['item_id'].astype(str)
    x = data.drop(['rating', 'user_id', 'item_id'], axis=1)
    y = data['rating']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(random_state=42)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    print(f"RMSE: {rmse}")
    example_context = pd.DataFrame([{col: 0 for col in x_train.columns}])
    example_context['user_item'] = '1_101'
    example_context['time_of_day_morning'] = 1
    example_context['weather_sunny'] = 1
    example_context = example_context[x_train.columns]
    example_prediction = model.predict(example_context)[0]
    print(f"Predicted Rating for the example context: {example_prediction}")